import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# ─── Page Config ───────────────────────────────────────────────
st.set_page_config(
    page_title="Mess Admin Dashboard",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded",
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

    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #E2E8F0;
    }
    section[data-testid="stSidebar"] .stMarkdown h1 {
        color: #0F172A;
        font-size: 1.3rem;
        font-weight: 700;
    }

    /* KPI card styling */
    .kpi-card {
        background: #ffffff;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 28px 32px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        border-top: 4px solid #2563EB;
        transition: box-shadow 0.2s;
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

    /* Chart container styling */
    .chart-container {
        background: #ffffff;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 32px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }
    .chart-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #0F172A;
        margin-bottom: 16px;
    }

    /* Table container styling */
    .table-container {
        background: #ffffff;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 32px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }
    .table-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #0F172A;
        margin-bottom: 16px;
    }

    /* Badge styling */
    .badge-good {
        background: #EFF6FF;
        color: #2563EB;
        padding: 4px 12px;
        border-radius: 999px;
        font-size: 0.75rem;
        font-weight: 600;
    }
    .badge-risk {
        background: #FEF2F2;
        color: #DC2626;
        padding: 4px 12px;
        border-radius: 999px;
        font-size: 0.75rem;
        font-weight: 600;
    }
    .badge-normal {
        background: #F1F5F9;
        color: #64748B;
        padding: 4px 12px;
        border-radius: 999px;
        font-size: 0.75rem;
        font-weight: 600;
    }

    /* Logout button */
    .logout-btn {
        color: #DC2626;
        font-weight: 500;
        font-size: 0.875rem;
        cursor: pointer;
        text-decoration: none;
    }

    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Reduce default padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    div[data-testid="stHorizontalBlock"] {
        gap: 1.5rem;
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
    {"meal": "Breakfast", "rice": 5, "dal": 3, "veg": 2},
    {"meal": "Lunch", "rice": 12, "dal": 8, "veg": 6},
    {"meal": "Dinner", "rice": 9, "dal": 6, "veg": 4},
]

dishes_data = [
    {"name": "Paneer Butter Masala", "rating": 4.2, "wastePercent": 6},
    {"name": "Dal Tadka", "rating": 4.5, "wastePercent": 3},
    {"name": "Veg Pulao", "rating": 3.8, "wastePercent": 10},
]


# ─── Sidebar ──────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 32px;">
        <div style="width: 36px; height: 36px; background: #2563EB; border-radius: 8px; display: flex; align-items: center; justify-content: center;">
            <span style="color: white; font-weight: 700; font-size: 14px;">M</span>
        </div>
        <span style="font-size: 1.2rem; font-weight: 700; color: #0F172A;">Mess Admin</span>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "Navigation",
        ["Dashboard", "Waste Analytics", "Menu Performance", "Settings"],
        label_visibility="collapsed",
    )


# ─── Navbar ───────────────────────────────────────────────────
col_title, col_spacer, col_user = st.columns([3, 5, 2])
with col_title:
    st.markdown(f"<h1 style='font-size: 1.5rem; font-weight: 700; color: #0F172A; margin: 0;'>{page}</h1>", unsafe_allow_html=True)
with col_user:
    st.markdown("""
    <div style="display: flex; align-items: center; justify-content: flex-end; gap: 12px;">
        <div style="width: 32px; height: 32px; background: #EFF6FF; border-radius: 50%; display: flex; align-items: center; justify-content: center;">
            <span style="color: #2563EB; font-size: 12px; font-weight: 600;">MA</span>
        </div>
        <span style="font-size: 0.875rem; font-weight: 500; color: #0F172A;">Mess Admin</span>
        <span class="logout-btn">Logout</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr style='border: none; border-top: 1px solid #E2E8F0; margin: 8px 0 32px 0;'>", unsafe_allow_html=True)


# ─── Dashboard Page ───────────────────────────────────────────
if page == "Dashboard":

    # ── KPI Cards ─────────────────────────────────────────────
    total_portions = today_data["portion"]["small"] + today_data["portion"]["regular"]

    k1, k2, k3, k4 = st.columns(4)

    with k1:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-value">{today_data['breakfast']}</div>
            <div class="kpi-title">Breakfast Confirmed</div>
            <div class="kpi-subtitle">Today's total</div>
        </div>
        """, unsafe_allow_html=True)

    with k2:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-value">{today_data['lunch']}</div>
            <div class="kpi-title">Lunch Confirmed</div>
            <div class="kpi-subtitle">Today's total</div>
        </div>
        """, unsafe_allow_html=True)

    with k3:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-value">{today_data['dinner']}</div>
            <div class="kpi-title">Dinner Confirmed</div>
            <div class="kpi-subtitle">Today's total</div>
        </div>
        """, unsafe_allow_html=True)

    with k4:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-value">{total_portions}</div>
            <div class="kpi-title">Total Portions</div>
            <div class="kpi-subtitle">Small: {today_data['portion']['small']} · Regular: {today_data['portion']['regular']}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)

    # ── Charts Row ────────────────────────────────────────────
    chart1, chart2 = st.columns([2, 1])

    with chart1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.markdown('<div class="chart-title">Weekly Demand Trend</div>', unsafe_allow_html=True)

        df_trend = pd.DataFrame(weekly_trend)
        fig_line = go.Figure()
        fig_line.add_trace(go.Scatter(
            x=df_trend["day"], y=df_trend["breakfast"],
            mode="lines+markers", name="Breakfast",
            line=dict(color="#93C5FD", width=2),
            marker=dict(size=7, color="#93C5FD"),
        ))
        fig_line.add_trace(go.Scatter(
            x=df_trend["day"], y=df_trend["lunch"],
            mode="lines+markers", name="Lunch",
            line=dict(color="#2563EB", width=2),
            marker=dict(size=7, color="#2563EB"),
        ))
        fig_line.add_trace(go.Scatter(
            x=df_trend["day"], y=df_trend["dinner"],
            mode="lines+markers", name="Dinner",
            line=dict(color="#DC2626", width=2),
            marker=dict(size=7, color="#DC2626"),
        ))
        fig_line.update_layout(
            plot_bgcolor="white",
            paper_bgcolor="white",
            margin=dict(l=0, r=0, t=10, b=0),
            height=300,
            legend=dict(orientation="h", yanchor="bottom", y=-0.25, xanchor="center", x=0.5),
            xaxis=dict(gridcolor="#E2E8F0", showline=False),
            yaxis=dict(gridcolor="#E2E8F0", showline=False),
            font=dict(family="Inter", color="#64748B"),
        )
        st.plotly_chart(fig_line, use_container_width=True, config={"displayModeBar": False})
        st.markdown('</div>', unsafe_allow_html=True)

    with chart2:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.markdown('<div class="chart-title">Portion Distribution</div>', unsafe_allow_html=True)

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
            margin=dict(l=0, r=0, t=10, b=0),
            height=300,
            legend=dict(orientation="h", yanchor="bottom", y=-0.15, xanchor="center", x=0.5),
            font=dict(family="Inter", color="#64748B"),
        )
        st.plotly_chart(fig_pie, use_container_width=True, config={"displayModeBar": False})
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)

    # ── Tables Row ────────────────────────────────────────────
    tab1, tab2 = st.columns(2)

    with tab1:
        st.markdown('<div class="table-container">', unsafe_allow_html=True)
        st.markdown('<div class="table-title">Waste Analysis</div>', unsafe_allow_html=True)

        df_waste = pd.DataFrame(waste_data)
        df_waste.columns = ["Meal", "Rice (kg)", "Dal (kg)", "Veg (kg)"]

        st.markdown(
            df_waste.to_html(index=False, classes="", border=0),
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="table-container">', unsafe_allow_html=True)
        st.markdown('<div class="table-title">Dish Performance</div>', unsafe_allow_html=True)

        def get_badge(row):
            if row["rating"] > 4.2:
                return f'<span class="badge-good">Good</span>'
            elif row["wastePercent"] > 8:
                return f'<span class="badge-risk">Risk</span>'
            return f'<span class="badge-normal">Normal</span>'

        rows_html = ""
        for dish in dishes_data:
            badge = get_badge(dish)
            rows_html += f"""
            <tr style="border-bottom: 1px solid #E2E8F0;">
                <td style="padding: 12px 16px; font-weight: 500; color: #0F172A;">{dish['name']}</td>
                <td style="padding: 12px 16px; color: #64748B;">{dish['rating']}</td>
                <td style="padding: 12px 16px; color: #64748B;">{dish['wastePercent']}%</td>
                <td style="padding: 12px 16px;">{badge}</td>
            </tr>
            """

        st.markdown(f"""
        <table style="width: 100%; border-collapse: collapse; font-size: 0.875rem;">
            <thead>
                <tr style="border-bottom: 1px solid #E2E8F0;">
                    <th style="text-align: left; padding: 12px 16px; font-weight: 600; color: #64748B;">Dish</th>
                    <th style="text-align: left; padding: 12px 16px; font-weight: 600; color: #64748B;">Rating</th>
                    <th style="text-align: left; padding: 12px 16px; font-weight: 600; color: #64748B;">Waste %</th>
                    <th style="text-align: left; padding: 12px 16px; font-weight: 600; color: #64748B;">Status</th>
                </tr>
            </thead>
            <tbody>
                {rows_html}
            </tbody>
        </table>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)


# ─── Placeholder Pages ────────────────────────────────────────
elif page == "Waste Analytics":
    st.markdown("### 🚧 Waste Analytics")
    st.info("This page is under development.")

elif page == "Menu Performance":
    st.markdown("### 🚧 Menu Performance")
    st.info("This page is under development.")

elif page == "Settings":
    st.markdown("### ⚙️ Settings")
    st.info("This page is under development.")
