def fetch_usgs_eq(start_date, end_date, minmag=4.5, bbox=None, limit=20000):
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    params = {
        "format": "geojson",
        "starttime": str(start_date),
        "endtime": str(end_date),
        "minmagnitude": float(minmag),
        "orderby": "time-asc",
        "limit": int(limit)
    }
    if bbox:
        params.update(dict(minlatitude=bbox[0], maxlatitude=bbox[1],
                           minlongitude=bbox[2], maxlongitude=bbox[3]))
    r = requests.get(url, params=params, timeout=60); r.raise_for_status()
    feats = r.json().get("features", [])
    rows = []
    for f in feats:
        p = f.get("properties", {})
        g = f.get("geometry", {}) or {}
        lon, lat, depth = (g.get("coordinates") or [None, None, None])[:3]
        rows.append({
            "id": f.get("id"),
            "time": pd.to_datetime(p.get("time"), unit="ms", utc=True),
            "title": p.get("place"),
            "lat": lat, "lon": lon,
            "mag": p.get("mag"),
            "depth_km": depth,
            "url": p.get("url")
        })
    df = pd.DataFrame(rows)
    if not df.empty:
        df["date"] = df["time"].dt.date
    return df

def fetch_eonet(status="open", limit=400):
    url = "https://eonet.gsfc.nasa.gov/api/v3/events"
    r = requests.get(url, params={"status": status, "limit": int(limit)}, timeout=60)
    r.raise_for_status()
    events = r.json().get("events", [])
    rows = []
    for ev in events:
        title = ev.get("title")
        cats = [c["title"] for c in ev.get("categories", [])]
        link = (ev.get("links") or [{}])[0].get("href")
        eid = ev.get("id")
        for geo in ev.get("geometry", []):
            coords = geo.get("coordinates")
            if not isinstance(coords, list) or len(coords) < 2: continue
            lon, lat = coords[0], coords[1]
            rows.append({
                "id": f"{eid}_{geo.get('date')}",
                "event_id": eid,
                "title": title,
                "categories": ", ".join(cats),
                "lat": lat, "lon": lon,
                "date": geo.get("date"),
                "url": link
            })
    return pd.DataFrame(rows)

def append_csv(path, df, key_cols):
    if df is None or df.empty:
        return pd.read_csv(path) if os.path.exists(path) else pd.DataFrame()
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        df.to_csv(path, index=False); return df
    old = pd.read_csv(path)
    all_df = pd.concat([old, df], ignore_index=True).drop_duplicates(subset=key_cols, keep="last")
    all_df.to_csv(path, index=False)
    return all_df