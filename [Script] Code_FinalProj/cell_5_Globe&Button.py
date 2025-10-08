def make_globe(eq, eo, title="Holographic Data Globe 🌍", animate=False):
    traces = []
    if eq is not None and not eq.empty:
        size_eq = np.clip((eq["mag"].fillna(0) - 3.5) * 4, 4, 20)
        text_eq = ("<b>Earthquake</b><br>" +
                   "M" + eq["mag"].round(1).astype(str) + " • " +
                   eq["title"].fillna("(unknown)") + "<br>" +
                   "Depth: " + eq["depth_km"].round(1).astype(str) + " km<br>" +
                   eq["time"].astype(str) + "<br>" +
                   "<a href='" + eq["url"].fillna("") + "' target='_blank'>USGS</a>")
        traces.append(go.Scattergeo(
            lon=eq["lon"], lat=eq["lat"], text=text_eq, hoverinfo="text",
            mode="markers", marker=dict(size=size_eq, color="red", opacity=0.72),
            name="Earthquakes"
        ))
    if eo is not None and not eo.empty:
        text_eo = ("<b>EONET</b><br>" + eo["title"].fillna("") + "<br>" +
                   eo["categories"].fillna("") + "<br>" + eo["date"].astype(str) + "<br>" +
                   "<a href='" + eo["url"].fillna("") + "' target='_blank'>More</a>")
        traces.append(go.Scattergeo(
            lon=eo["lon"], lat=eo["lat"], text=text_eo, hoverinfo="text",
            mode="markers", marker=dict(size=6, color="orange", opacity=0.75, symbol="triangle-up"),
            name="Wildfires / EONET"
        ))

    layout = go.Layout(
        title=title,
        geo=dict(
            projection_type="orthographic",
            showland=True, landcolor="rgb(230,230,230)",
            showocean=True, oceancolor="rgb(200, 220, 255)",
            showcountries=True, countrycolor="rgb(180,180,180)",
            lonaxis=dict(showgrid=True, gridcolor="rgba(0,0,0,0.1)"),
            lataxis=dict(showgrid=True, gridcolor="rgba(0,0,0,0.1)"),
        ),
        legend=dict(x=0.02, y=0.02),
        margin=dict(l=0, r=0, t=50, b=0)
    )
    fig = go.Figure(data=traces, layout=layout)

    names = [tr.name for tr in traces]
    def vis_mask(active): return [(tr.name == active) for tr in traces]
    buttons = [dict(label="All", method="update",
                    args=[{"visible":[True]*len(traces)}, {"title": title+" — All"}])]
    for nm in names:
        buttons.append(dict(label=nm, method="update",
                            args=[{"visible": vis_mask(nm)}, {"title": title+f" — {nm}"}]))
    fig.update_layout(updatemenus=[dict(type="dropdown", x=0.02, y=0.98, buttons=buttons)])

    # --- Timeline Animation (Earthquakes by day) ---
    if animate and (eq is not None) and not eq.empty:
        # สร้างเฟรมตามวัน
        eq_sorted = eq.sort_values("time")
        eq_sorted["day"] = eq_sorted["time"].dt.date
        frames = []
        days = sorted(eq_sorted["day"].unique())

        for d in days:
            chunk = eq_sorted[eq_sorted["day"] <= d]
            size = np.clip((chunk["mag"].fillna(0) - 3.5) * 4, 4, 20)
            text = ("<b>Earthquake</b><br>"
                    "M" + chunk["mag"].round(1).astype(str) + " • " +
                    chunk["title"].fillna("(unknown)") + "<br>" +
                    "Depth: " + chunk["depth_km"].round(1).astype(str) + " km<br>" +
                    chunk["time"].astype(str))

            # อัปเดตเฉพาะ trace ที่ 0 (Earthquakes)
            frames.append(go.Frame(
                data=[go.Scattergeo(
                    lon=chunk["lon"], lat=chunk["lat"],
                    marker=dict(size=size), mode="markers",
                    text=text, hoverinfo="text"
                )],
                traces=[0],   # <— สำคัญ: อัปเดตเฉพาะเลเยอร์ EQ
                name=str(d)
            ))

        fig.frames = frames

    return fig

def eq_daily_stats(eq):
    if eq is None or eq.empty: return pd.DataFrame()
    g = eq.groupby(eq["time"].dt.date).agg(
        count=("id","count"), mag_mean=("mag","mean"), mag_max=("mag","max")
    ).reset_index().rename(columns={"time":"date"})
    return g

def eq_latlon_bins(eq, bins=24):
    if eq is None or eq.empty:
        return pd.DataFrame(columns=["lat_c","lon_c","count"])
    work = eq.dropna(subset=["lat","lon"])
    if work.empty:
        return pd.DataFrame(columns=["lat_c","lon_c","count"])
    lat_bins = pd.cut(work["lat"], bins=bins)
    lon_bins = pd.cut(work["lon"], bins=bins)
    h = work.groupby([lat_bins, lon_bins]).size().reset_index(name="count")
    h["lat_c"] = h["lat"].apply(lambda b: float((b.left + b.right)/2) if pd.notna(b) else None)
    h["lon_c"] = h["lon"].apply(lambda b: float((b.left + b.right)/2) if pd.notna(b) else None)
    return h[["lat_c","lon_c","count"]].sort_values("count", ascending=False).reset_index(drop=True)