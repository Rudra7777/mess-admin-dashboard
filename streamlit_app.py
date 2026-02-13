import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# ─── Page Config ───────────────────────────────────────────────
st.set_page_config(
    page_title="Mess Admin Dashboard",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── Custom CSS ────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background-color: #F8FAFC;
    }

    /* Hide sidebar completely */
    section[data-testid="stSidebar"] {
        display: none !important;
    }
    button[kind="header"] {
        display: none !important;
    }

    /* KPI card */
    .kpi-card {
        background: #ffffff;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 28px 32px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        border-top: 4px solid #2563EB;
        transition: box-shadow 0.2s;
        height: 100%;
    }
    .kpi-card:hover {
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }
    .kpi-value {
        font-size: 2.2rem;
        font-weight: 700;
        color: #0F172A;
        line-height: 1.2;
    }
    .kpi-title {
        font-size: 0.875rem;
        font-weight: 500;
        color: #64748B;
        margin-top: 4px;
    }
    .kpi-subtitle {
        font-size: 0.75rem;
        color: #94A3B8;
        margin-top: 8px;
    }

    /* Chart / table containers */
    .card-box {
        background: #ffffff;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 32px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }
    .section-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #0F172A;
        margin-bottom: 16px;
    }

    /* Styled table */
    .styled-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 0.875rem;
    }
    .styled-table th {
        text-align: left;
        padding: 12px 16px;
        font-weight: 600;
        color: #64748B;
        border-bottom: 1px solid #E2E8F0;
    }
    .styled-table td {
        padding: 12px 16px;
        color: #334155;
        border-bottom: 1px solid #F1F5F9;
    }
    .styled-table tr:last-child td {
        border-bottom: none;
    }
    .styled-table tr:hover td {
        background: #F8FAFC;
    }

    /* Badges */
    .badge-good {
        background: #EFF6FF; color: #2563EB;
        padding: 4px 12px; border-radius: 999px;
        font-size: 0.75rem; font-weight: 600;
    }
    .badge-risk {
        background: #FEF2F2; color: #DC2626;
        padding: 4px 12px; border-radius: 999px;
        font-size: 0.75rem; font-weight: 600;
    }
    .badge-normal {
        background: #F1F5F9; color: #64748B;
        padding: 4px 12px; border-radius: 999px;
        font-size: 0.75rem; font-weight: 600;
    }

    /* Hide Streamlit defaults */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }
</style>
""", unsafe_allow_html=True)


# ─── Dummy Data ────────────────────────────────────────────────
today_data = {
    "breakfast": 180,
    "lunch": 210,
    "dinner": 195,
    "portion": {"small": 120, "regular": 465},
}

weekly_trend = [
    {"day": "Mon", "breakfast": 160, "lunch": 190, "dinner": 180},
    {"day": "Tue", "breakfast": 170, "lunch": 200, "dinner": 185},
    {"day": "Wed", "breakfast": 150, "lunch": 185, "dinner": 170},
    {"day": "Thu", "breakfast": 180, "lunch": 210, "dinner": 195},
    {"day": "Fri", "breakfast": 190, "lunch": 230, "dinner": 200},
    {"day": "Sat", "breakfast": 170, "lunch": 195, "dinner": 175},
    {"day": "Sun", "breakfast": 140, "lunch": 170, "dinner": 160},
]

waste_data = [
    {"Meal": "Breakfast", "Rice (kg)": 5, "Dal (kg)": 3, "Veg (kg)": 2},
    {"Meal": "Lunch", "Rice (kg)": 12, "Dal (kg)": 8, "Veg (kg)": 6},
    {"Meal": "Dinner", "Rice (kg)": 9, "Dal (kg)": 6, "Veg (kg)": 4},
]

dishes_data = [
    {"name": "Paneer Butter Masala", "rating": 4.2, "wastePercent": 6},
    {"name": "Dal Tadka", "rating": 4.5, "wastePercent": 3},
    {"name": "Veg Pulao", "rating": 3.8, "wastePercent": 10},
]


# ─── Header Bar ───────────────────────────────────────────────
col_title, col_user = st.columns([8, 2])
with col_title:
    st.markdown("<h1 style='font-size:1.5rem; font-weight:700; color:#0F172A; margin:0;'>🍽️ Mess Admin Dashboard</h1>", unsafe_allow_html=True)
with col_user:
    st.markdown("""
    <div style="display:flex; align-items:center; justify-content:flex-end; gap:10px; padding-top:4px;">
        <div style="width:32px; height:32px; background:#EFF6FF; border-radius:50%; display:flex; align-items:center; justify-content:center;">
            <span style="color:#2563EB; font-size:12px; font-weight:600;">MA</span>
        </div>
        <span style="font-size:0.85rem; font-weight:500; color:#0F172A;">Mess Admin</span>
        <span style="color:#DC2626; font-size:0.85rem; font-weight:500; cursor:pointer;">Logout</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr style='border:none; border-top:1px solid #E2E8F0; margin:8px 0 32px 0;'>", unsafe_allow_html=True)


# ─── KPI Cards ────────────────────────────────────────────────
total_portions = today_data["portion"]["small"] + today_data["portion"]["regular"]

kpis = [
    {"value": today_data["breakfast"], "title": "Breakfast Confirmed", "sub": "Today's total"},
    {"value": today_data["lunch"], "title": "Lunch Confirmed", "sub": "Today's total"},
    {"value": today_data["dinner"], "title": "Dinner Confirmed", "sub": "Today's total"},
    {"value": total_portions, "title": "Total Portions", "sub": f"Small: {today_data['portion']['small']} · Regular: {today_data['portion']['regular']}"},
]

cols = st.columns(4)
for i, kpi in enumerate(kpis):
    with cols[i]:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-value">{kpi['value']}</div>
            <div class="kpi-title">{kpi['title']}</div>
            <div class="kpi-subtitle">{kpi['sub']}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<div style='height:40px;'></div>", unsafe_allow_html=True)


# ─── Charts Row ───────────────────────────────────────────────
chart1, chart2 = st.columns([2, 1])

with chart1:
    st.markdown('<div class="card-box"><div class="section-title">Weekly Demand Trend</div>', unsafe_allow_html=True)

    df_trend = pd.DataFrame(weekly_trend)
    fig_line = go.Figure()
    for name, color in [("breakfast", "#93C5FD"), ("lunch", "#2563EB"), ("dinner", "#DC2626")]:
        fig_line.add_trace(go.Scatter(
            x=df_trend["day"], y=df_trend[name],
            mode="lines+markers", name=name.capitalize(),
            line=dict(color=color, width=2),
            marker=dict(size=7, color=color),
        ))
    fig_line.update_layout(
        plot_bgcolor="white", paper_bgcolor="white",
        margin=dict(l=0, r=0, t=10, b=0), height=300,
        legend=dict(orientation="h", yanchor="bottom", y=-0.25, xanchor="center", x=0.5, font=dict(size=13, color="#0F172A")),
        xaxis=dict(gridcolor="#E2E8F0", showline=False, tickfont=dict(size=12, color="#0F172A")),
        yaxis=dict(gridcolor="#E2E8F0", showline=False, tickfont=dict(size=12, color="#0F172A")),
        font=dict(family="Inter", color="#0F172A"),
    )
    st.plotly_chart(fig_line, use_container_width=True, config={"displayModeBar": False})
    st.markdown('</div>', unsafe_allow_html=True)

with chart2:
    st.markdown('<div class="card-box"><div class="section-title">Portion Distribution</div>', unsafe_allow_html=True)

    fig_pie = go.Figure(data=[go.Pie(
        labels=["Regular", "Small"],
        values=[today_data["portion"]["regular"], today_data["portion"]["small"]],
        hole=0.55,
        marker=dict(colors=["#DC2626", "#2563EB"]),
        textinfo="percent",
        textfont=dict(size=14, color="white", family="Inter"),
    )])
    fig_pie.update_layout(
        paper_bgcolor="white",
        margin=dict(l=0, r=0, t=10, b=0), height=300,
        legend=dict(orientation="h", yanchor="bottom", y=-0.15, xanchor="center", x=0.5, font=dict(size=13, color="#0F172A")),
        font=dict(family="Inter", color="#0F172A"),
    )
    st.plotly_chart(fig_pie, use_container_width=True, config={"displayModeBar": False})
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<div style='height:40px;'></div>", unsafe_allow_html=True)


# ─── Tables Row ───────────────────────────────────────────────
tab1, tab2 = st.columns(2)

with tab1:
    # Build waste table HTML
    waste_rows = ""
    for row in waste_data:
        waste_rows += f"""<tr>
            <td style="font-weight:500;">{row['Meal']}</td>
            <td>{row['Rice (kg)']}</td>
            <td>{row['Dal (kg)']}</td>
            <td>{row['Veg (kg)']}</td>
        </tr>"""

    st.markdown(f"""
    <div class="card-box">
        <div class="section-title">Waste Analysis</div>
        <table class="styled-table">
            <thead>
                <tr>
                    <th>Meal</th>
                    <th>Rice (kg)</th>
                    <th>Dal (kg)</th>
                    <th>Veg (kg)</th>
                </tr>
            </thead>
            <tbody>{waste_rows}</tbody>
        </table>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    # Build dish performance table HTML
    dish_rows = ""
    for dish in dishes_data:
        if dish["rating"] > 4.2:
            badge = '<span class="badge-good">Good</span>'
        elif dish["wastePercent"] > 8:
            badge = '<span class="badge-risk">Risk</span>'
        else:
            badge = '<span class="badge-normal">Normal</span>'

        dish_rows += f"""<tr>
            <td style="font-weight:500;">{dish['name']}</td>
            <td>{dish['rating']}</td>
            <td>{dish['wastePercent']}%</td>
            <td>{badge}</td>
        </tr>"""

    st.markdown(f"""
    <div class="card-box">
        <div class="section-title">Dish Performance</div>
        <table class="styled-table">
            <thead>
                <tr>
                    <th>Dish</th>
                    <th>Rating</th>
                    <th>Waste %</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>{dish_rows}</tbody>
        </table>
    </div>
    """, unsafe_allow_html=True)
