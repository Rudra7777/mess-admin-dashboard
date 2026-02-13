export const dashboardData = {
    today: {
        breakfast: 180,
        lunch: 210,
        dinner: 195,
        portion: {
            small: 120,
            regular: 465,
        },
    },
    weeklyTrend: [
        { day: "Mon", breakfast: 160, lunch: 200, dinner: 180 },
        { day: "Tue", breakfast: 170, lunch: 210, dinner: 190 },
        { day: "Wed", breakfast: 150, lunch: 190, dinner: 175 },
        { day: "Thu", breakfast: 180, lunch: 220, dinner: 200 },
        { day: "Fri", breakfast: 190, lunch: 230, dinner: 210 },
        { day: "Sat", breakfast: 140, lunch: 180, dinner: 160 },
        { day: "Sun", breakfast: 120, lunch: 150, dinner: 140 },
    ],
    waste: [
        { meal: "Breakfast", rice: 5, dal: 3, veg: 2 },
        { meal: "Lunch", rice: 12, dal: 8, veg: 6 },
        { meal: "Dinner", rice: 9, dal: 6, veg: 4 },
    ],
    dishes: [
        { name: "Paneer Butter Masala", rating: 4.2, wastePercent: 6 },
        { name: "Dal Tadka", rating: 4.5, wastePercent: 3 },
        { name: "Veg Pulao", rating: 3.8, wastePercent: 10 },
    ],
};
