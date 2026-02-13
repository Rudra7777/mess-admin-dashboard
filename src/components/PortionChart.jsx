import { PieChart, Pie, Cell, ResponsiveContainer, Legend, Tooltip } from "recharts";

const COLORS = ["#2563EB", "#DC2626"];

const RADIAN = Math.PI / 180;
function renderLabel({ cx, cy, midAngle, innerRadius, outerRadius, percent }) {
    const radius = innerRadius + (outerRadius - innerRadius) * 0.5;
    const x = cx + radius * Math.cos(-midAngle * RADIAN);
    const y = cy + radius * Math.sin(-midAngle * RADIAN);
    return (
        <text
            x={x}
            y={y}
            fill="white"
            textAnchor="middle"
            dominantBaseline="central"
            className="text-sm font-semibold"
        >
            {`${(percent * 100).toFixed(0)}%`}
        </text>
    );
}

export default function PortionChart({ data }) {
    const chartData = [
        { name: "Small", value: data.small },
        { name: "Regular", value: data.regular },
    ];

    return (
        <div className="bg-card rounded-xl shadow-sm border border-border" style={{ padding: '32px' }}>
            <h2 className="text-lg font-bold text-text-primary mb-6">
                Portion Distribution
            </h2>
            <div className="h-72" style={{ minWidth: 0 }}>
                <ResponsiveContainer width="100%" height="100%" minWidth={0}>
                    <PieChart>
                        <Pie
                            data={chartData}
                            cx="50%"
                            cy="50%"
                            innerRadius={60}
                            outerRadius={100}
                            paddingAngle={4}
                            dataKey="value"
                            labelLine={false}
                            label={renderLabel}
                        >
                            {chartData.map((_, index) => (
                                <Cell key={`cell-${index}`} fill={COLORS[index]} />
                            ))}
                        </Pie>
                        <Tooltip />
                        <Legend />
                    </PieChart>
                </ResponsiveContainer>
            </div>
        </div>
    );
}
