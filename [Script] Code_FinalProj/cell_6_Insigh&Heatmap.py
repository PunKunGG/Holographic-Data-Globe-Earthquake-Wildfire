def eq_daily_stats(eq: pd.DataFrame):
    if eq is None or eq.empty: return pd.DataFrame()
    g = eq.groupby(eq["time"].dt.date).agg(
        count=("id","count"), mag_mean=("mag","mean"), mag_max=("mag","max")
    ).reset_index().rename(columns={"time":"date"})
    return g

def eq_latlon_bins(eq: pd.DataFrame, bins=24):
    """
    คืนตาราง heatmap ที่ serialize ง่าย: lat_c, lon_c, count (ตัวเลขล้วน)
    """
    if eq is None or eq.empty:
        return pd.DataFrame(columns=["lat_c","lon_c","count"])
    # drop NA ก่อน
    work = eq.dropna(subset=["lat","lon"])
    if work.empty:
        return pd.DataFrame(columns=["lat_c","lon_c","count"])

    lat_bins = pd.cut(work["lat"], bins=bins)
    lon_bins = pd.cut(work["lon"], bins=bins)
    h = work.groupby([lat_bins, lon_bins]).size().reset_index(name="count")

    # จุดกลางของ bin เป็นตัวเลข
    h["lat_c"] = h["lat"].apply(lambda b: float((b.left + b.right)/2) if pd.notna(b) else None)
    h["lon_c"] = h["lon"].apply(lambda b: float((b.left + b.right)/2) if pd.notna(b) else None)

    # คืนเฉพาะคอลัมน์ตัวเลข
    return h[["lat_c","lon_c","count"]].sort_values("count", ascending=False).reset_index(drop=True)