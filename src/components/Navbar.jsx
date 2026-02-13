export default function Navbar({ onMenuToggle }) {
    return (
        <header className="h-16 bg-white border-b border-border flex items-center justify-between sticky top-0 z-30" style={{ padding: '0 48px' }}>
            <div className="flex items-center gap-4">
                {/* Hamburger toggle - always visible */}
                <button
                    onClick={onMenuToggle}
                    className="p-2 rounded-md text-text-secondary hover:text-text-primary hover:bg-gray-100 cursor-pointer"
                >
                    <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
                    </svg>
                </button>
                <h1 className="text-xl font-bold text-text-primary">Dashboard</h1>
            </div>

            <div className="flex items-center gap-4">
                <div className="flex items-center gap-3">
                    <div className="w-8 h-8 bg-blue-50 rounded-full flex items-center justify-center">
                        <span className="text-blue text-sm font-semibold">MA</span>
                    </div>
                    <span className="text-sm font-medium text-text-primary hidden sm:block">
                        Mess Admin
                    </span>
                </div>
                <button className="text-sm font-medium text-red hover:text-red/80 transition-colors cursor-pointer">
                    Logout
                </button>
            </div>
        </header>
    );
}
