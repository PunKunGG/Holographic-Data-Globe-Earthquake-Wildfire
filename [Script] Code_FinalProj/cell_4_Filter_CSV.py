def load_filtered_data(start_date, end_date, min_mag, max_depth_km=None, region_bbox=None, eonet_category=None):
    eq = pd.read_csv(EQ_CSV, parse_dates=["time"]) if os.path.exists(EQ_CSV) else pd.DataFrame()
    eo = pd.read_csv(EONET_CSV) if os.path.exists(EONET_CSV) else pd.DataFrame()

    # Earthquakes filter
    if not eq.empty:
        eq = eq[(eq["time"].dt.date >= start_date) & (eq["time"].dt.date <= end_date)]
        eq["mag"] = pd.to_numeric(eq["mag"], errors="coerce")
        eq["depth_km"] = pd.to_numeric(eq["depth_km"], errors="coerce")
        eq = eq[eq["mag"].fillna(0) >= float(min_mag)]
        if max_depth_km is not None:
            eq = eq[eq["depth_km"].fillna(9e9) <= float(max_depth_km)]
        if region_bbox:
            minlat,maxlat,minlon,maxlon = region_bbox
            eq = eq[(eq["lat"]>=minlat)&(eq["lat"]<=maxlat)&(eq["lon"]>=minlon)&(eq["lon"]<=maxlon)]

    # EONET filter
    if not eo.empty:
        eo_dt = pd.to_datetime(eo["date"], errors="coerce").dt.date
        keep = (eo_dt >= start_date) & (eo_dt <= end_date)
        eo = eo[keep]
        if region_bbox:
            minlat,maxlat,minlon,maxlon = region_bbox
            eo = eo[(eo["lat"]>=minlat)&(eo["lat"]<=maxlat)&(eo["lon"]>=minlon)&(eo["lon"]<=maxlon)]
        if eonet_category and eonet_category!="All":
            eo = eo[eo["categories"].str.contains(eonet_category, na=False)]

    return eq, eo