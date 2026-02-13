export default function WasteTable({ data }) {
    return (
        <div className="bg-card rounded-xl shadow-sm border border-border" style={{ padding: '32px' }}>
            <h2 className="text-lg font-bold text-text-primary mb-6">
                Waste Analysis
            </h2>
            <div className="overflow-x-auto">
                <table className="w-full text-sm">
                    <thead>
                        <tr className="border-b border-border">
                            <th className="text-left py-3 px-4 font-semibold text-text-secondary">
                                Meal
                            </th>
                            <th className="text-left py-3 px-4 font-semibold text-text-secondary">
                                Rice (kg)
                            </th>
                            <th className="text-left py-3 px-4 font-semibold text-text-secondary">
                                Dal (kg)
                            </th>
                            <th className="text-left py-3 px-4 font-semibold text-text-secondary">
                                Veg (kg)
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        {data.map((row) => (
                            <tr
                                key={row.meal}
                                className="border-b border-border last:border-0 hover:bg-gray-50 transition-colors"
                            >
                                <td className="py-3 px-4 font-medium text-text-primary">
                                    {row.meal}
                                </td>
                                <td className="py-3 px-4 text-text-secondary">{row.rice}</td>
                                <td className="py-3 px-4 text-text-secondary">{row.dal}</td>
                                <td className="py-3 px-4 text-text-secondary">{row.veg}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
}
