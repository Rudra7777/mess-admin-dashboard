export default function KPIcard({ title, value, subtitle }) {
    return (
        <div className="bg-card rounded-xl shadow-sm border border-border overflow-hidden hover:shadow-md transition-shadow">
            <div className="h-1 bg-blue" />
            <div style={{ padding: '24px 32px' }}>
                <p className="text-3xl font-bold text-text-primary">{value}</p>
                <p className="text-sm font-medium text-text-secondary mt-1">{title}</p>
                {subtitle && (
                    <p className="text-xs text-text-secondary mt-2">{subtitle}</p>
                )}
            </div>
        </div>
    );
}
