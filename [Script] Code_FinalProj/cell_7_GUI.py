def refresh_and_store(start_str, end_str, min_mag, region_name, fetch_new, max_depth, eonet_category,
                      animate, alert_threshold, line_token, tg_bot, tg_chat):
    # parse date
    try:
        start_date = dt.date.fromisoformat(str(start_str))
        end_date   = dt.date.fromisoformat(str(end_str))
    except Exception as e:
        return None, f"❌ Invalid date (YYYY-MM-DD). {e}", pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

    min_mag = float(min_mag or 0)
    max_depth = float(max_depth or 0)
    bbox = REGIONS.get(region_name)

    # fetch & store (CSV only)
    if fetch_new:
        try:
            eq_new = fetch_usgs_eq(start_date, end_date, minmag=min_mag, bbox=bbox)
            eo_new = fetch_eonet(status="open", limit=600)
            append_csv(EQ_CSV, eq_new, ["id"])
            append_csv(EONET_CSV, eo_new, ["id"])
        except Exception as e:
            return None, f"❌ Fetch/CSV failed: {e}", pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

    # load from CSV with filters
    try:
        eq, eo = load_filtered_data(start_date, end_date, min_mag,
                                    max_depth_km=(max_depth if max_depth>0 else None),
                                    region_bbox=bbox, eonet_category=eonet_category)
    except Exception as e:
        return None, f"❌ Load/filter failed: {e}", pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

    # alerts
    alert_msg = "No alerts"
    try:
        thr = float(alert_threshold or 0)
        if thr > 0 and not eq.empty and "mag" in eq.columns:
            highlights = eq[eq["mag"] >= thr]
            if not highlights.empty:
                msg = f"⚠️ EQ ≥ {thr}: {len(highlights)} events\n" + \
                      highlights.sort_values("mag", ascending=False).head(5).apply(
                        lambda r: f"M{r['mag']:.1f} @ ({r['lat']:.2f},{r['lon']:.2f}) {str(r['title'])}", axis=1
                      ).str.cat(sep="\n")
                ln = line_notify(line_token, msg) if line_token else "LINE: skipped"
                tg = telegram_notify(tg_bot, tg_chat, msg) if (tg_bot and tg_chat) else "TG: skipped"
                alert_msg = f"{ln} | {tg}"
    except Exception as e:
        alert_msg = f"Alert error: {e}"

    # figure + outputs
    try:
        fig = make_globe(eq, eo, animate=bool(animate))
    except Exception as e:
        return None, f"❌ Figure failed: {e}", pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

    try:
        summary_df = pd.DataFrame([{
            "EQ_total": int(len(eq)) if not eq.empty else 0,
            "EQ_M≥6": int(eq["mag"].ge(6).sum()) if ("mag" in eq.columns and not eq.empty) else 0,
            "EQ_avgMag": round(float(eq["mag"].mean()), 2) if ("mag" in eq.columns and not eq.empty) else None,
            "EONET_total": int(len(eo)) if not eo.empty else 0
        }])
        daily = eq_daily_stats(eq)
        bins = eq_latlon_bins(eq, bins=24)
    except Exception as e:
        return fig, f"{alert_msg}\n(Insight error: {e})", pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

    return fig, alert_msg, summary_df, daily, bins

with gr.Blocks(title="Holographic Data Globe — CSV Only") as app:
    gr.Markdown("## 🌍 Holographic Data Globe — Earthquake & Wildfire")
    with gr.Row():
        start_in = gr.Textbox(value=str(dt.date.today()-dt.timedelta(days=7)), label="Start date (YYYY-MM-DD)")
        end_in   = gr.Textbox(value=str(dt.date.today()), label="End date (YYYY-MM-DD)")
        region   = gr.Dropdown(choices=list(REGIONS.keys()), value="Global", label="Region")
        minmag   = gr.Number(value=4.5, label="Min Magnitude (EQ)")
        maxdepth = gr.Number(value=0, label="Max Depth km (0=No limit)")
    with gr.Row():
        eocat    = gr.Dropdown(choices=["All","Wildfires","Severe Storms","Volcanoes","Icebergs","Drought"], value="All", label="EONET Category")
        animate  = gr.Checkbox(value=True, label="Timeline Animation (EQ)")
        fetchbtn = gr.Checkbox(value=True, label="Fetch & append to CSV now")
    with gr.Row():
        alert_thr= gr.Number(value=6.0, label="Alert when EQ ≥ (0=off)")
    run_btn = gr.Button("Render / Update")
    export_btn = gr.Button("Export HTML")

    out_fig  = gr.Plot(label="Interactive Globe")
    out_alert= gr.Markdown(label="Alerts")
    out_sum  = gr.Dataframe(label="Summary", interactive=False)
    out_daily= gr.Dataframe(label="EQ Daily Stats", interactive=False)
    out_bins = gr.Dataframe(label="EQ Lat/Lon Bins (for heatmap)", interactive=False)
    export_info = gr.Markdown()

    def on_export(fig):
        path = "globe_export.html"
        fig.write_html(path, include_plotlyjs="cdn")
        return f"✅ Exported: `./{path}` (ดาวน์โหลดได้จากแถบ Files)"

    run_btn.click(refresh_and_store,
                  inputs=[start_in, end_in, minmag, region, fetchbtn, maxdepth, eocat, animate,
                          alert_thr, line_tok, tg_bot, tg_chat],
                  outputs=[out_fig, out_alert, out_sum, out_daily, out_bins])

    export_btn.click(on_export, inputs=[out_fig], outputs=[export_info])

app.launch(debug=False)