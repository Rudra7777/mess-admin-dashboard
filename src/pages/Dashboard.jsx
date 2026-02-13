import { useState, useEffect } from "react";
import { dashboardData } from "../data/dummyData";
import KPIcard from "../components/KPIcard";
import DemandChart from "../components/DemandChart";
import PortionChart from "../components/PortionChart";
import WasteTable from "../components/WasteTable";
import DishPerformanceTable from "../components/DishPerformanceTable";

export default function Dashboard() {
    const [data, setData] = useState(null);

    useEffect(() => {
        setData(dashboardData);
    }, []);

    if (!data) return null;

    const totalPortions = data.today.portion.small + data.today.portion.regular;

    return (
        <div style={{ padding: '32px 48px', display: 'flex', flexDirection: 'column', gap: '56px' }}>
            {/* KPI Cards */}
            <div className="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-8">
                <KPIcard
                    title="Breakfast Confirmed"
                    value={data.today.breakfast}
                    subtitle="Today's total"
                />
                <KPIcard
                    title="Lunch Confirmed"
                    value={data.today.lunch}
                    subtitle="Today's total"
                />
                <KPIcard
                    title="Dinner Confirmed"
                    value={data.today.dinner}
                    subtitle="Today's total"
                />
                <KPIcard
                    title="Total Portions"
                    value={totalPortions}
                    subtitle={`Small: ${data.today.portion.small} · Regular: ${data.today.portion.regular}`}
                />
            </div>

            {/* Charts Row */}
            <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
                <div className="lg:col-span-2">
                    <DemandChart data={data.weeklyTrend} />
                </div>
                <div>
                    <PortionChart data={data.today.portion} />
                </div>
            </div>

            {/* Tables Row */}
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
                <WasteTable data={data.waste} />
                <DishPerformanceTable data={data.dishes} />
            </div>
        </div>
    );
}
