import {
    LineChart,
    Line,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    ResponsiveContainer,
    Legend,
} from "recharts";

export default function DemandChart({ data }) {
    return (
        <div className="bg-card rounded-xl shadow-sm border border-border" style={{ padding: '32px' }}>
            <h2 className="text-lg font-bold text-text-primary mb-6">
                Weekly Demand Trend
            </h2>
            <div className="h-72" style={{ minWidth: 0 }}>
                <ResponsiveContainer width="100%" height="100%" minWidth={0}>
                    <LineChart data={data}>
                        <CartesianGrid strokeDasharray="3 3" stroke="#E2E8F0" />
                        <XAxis
                            dataKey="day"
                            tick={{ fill: "#64748B", fontSize: 13 }}
                            axisLine={{ stroke: "#E2E8F0" }}
                            tickLine={false}
                        />
                        <YAxis
                            tick={{ fill: "#64748B", fontSize: 13 }}
                            axisLine={{ stroke: "#E2E8F0" }}
                            tickLine={false}
                        />
                        <Tooltip
                            contentStyle={{
                                borderRadius: "8px",
                                border: "1px solid #E2E8F0",
                                boxShadow: "0 1px 3px rgba(0,0,0,0.1)",
                            }}
                        />
                        <Legend />
                        <Line
                            type="monotone"
                            dataKey="breakfast"
                            stroke="#93C5FD"
                            strokeWidth={2}
                            dot={{ r: 4, fill: "#93C5FD" }}
                            name="Breakfast"
                        />
                        <Line
                            type="monotone"
                            dataKey="lunch"
                            stroke="#2563EB"
                            strokeWidth={2}
                            dot={{ r: 4, fill: "#2563EB" }}
                            name="Lunch"
                        />
                        <Line
                            type="monotone"
                            dataKey="dinner"
                            stroke="#DC2626"
                            strokeWidth={2}
                            dot={{ r: 4, fill: "#DC2626" }}
                            name="Dinner"
                        />
                    </LineChart>
                </ResponsiveContainer>
            </div>
        </div>
    );
}
