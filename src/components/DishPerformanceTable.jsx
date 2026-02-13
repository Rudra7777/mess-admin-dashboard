function getStatus(rating, wastePercent) {
    if (rating > 4.2) return { label: "Good", color: "bg-blue-50 text-blue" };
    if (wastePercent > 8) return { label: "Risk", color: "bg-red-50 text-red" };
    return { label: "Normal", color: "bg-gray-100 text-text-secondary" };
}

export default function DishPerformanceTable({ data }) {
    return (
        <div className="bg-card rounded-xl shadow-sm border border-border" style={{ padding: '32px' }}>
            <h2 className="text-lg font-bold text-text-primary mb-6">
                Dish Performance
            </h2>
            <div className="overflow-x-auto">
                <table className="w-full text-sm">
                    <thead>
                        <tr className="border-b border-border">
                            <th className="text-left py-3 px-4 font-semibold text-text-secondary">
                                Dish
                            </th>
                            <th className="text-left py-3 px-4 font-semibold text-text-secondary">
                                Rating
                            </th>
                            <th className="text-left py-3 px-4 font-semibold text-text-secondary">
                                Waste %
                            </th>
                            <th className="text-left py-3 px-4 font-semibold text-text-secondary">
                                Status
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        {data.map((dish) => {
                            const status = getStatus(dish.rating, dish.wastePercent);
                            return (
                                <tr
                                    key={dish.name}
                                    className="border-b border-border last:border-0 hover:bg-gray-50 transition-colors"
                                >
                                    <td className="py-3 px-4 font-medium text-text-primary">
                                        {dish.name}
                                    </td>
                                    <td className="py-3 px-4 text-text-secondary">
                                        {dish.rating}
                                    </td>
                                    <td className="py-3 px-4 text-text-secondary">
                                        {dish.wastePercent}%
                                    </td>
                                    <td className="py-3 px-4">
                                        <span
                                            className={`inline-block px-3 py-1 rounded-full text-xs font-semibold ${status.color}`}
                                        >
                                            {status.label}
                                        </span>
                                    </td>
                                </tr>
                            );
                        })}
                    </tbody>
                </table>
            </div>
        </div>
    );
}
