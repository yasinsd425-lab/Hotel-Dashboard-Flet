import flet as ft

def main(page: ft.Page):
    # --- تنظیمات صفحه ---
    page.title = "HotelOps Executive"
    page.theme_mode = "dark"
    page.padding = 0
    page.spacing = 0
    page.bgcolor = "#000000"
    page.scroll = "auto" # اسکرول اصلی

    # --- پالت رنگ (Hex Code برای جلوگیری از ارور) ---
    glass_bg = "#B3101216"      
    card_glass = "#801A1D24"    
    border_color = "#4DFFFFFF"  
    accent_color = "cyan"
    text_muted = "#B0B3B8"
    
    badge_green = "#334CAF50"
    badge_orange = "#33FF9800"
    badge_red = "#33F44336"

    # --- داده‌ها ---
    properties_data = [
        {"name": "St Kilda Esplanade", "loc": "Melbourne", "occ": "94%", "rev": "$24,500", "status": "Clean Data"},
        {"name": "Sydney Harbour", "loc": "Sydney", "occ": "88%", "rev": "$31,200", "status": "Clean Data"},
        {"name": "Gold Coast Resort", "loc": "Gold Coast", "occ": "98%", "rev": "$45,000", "status": "Xero Sync"},
        {"name": "Adelaide Heritage", "loc": "Adelaide", "occ": "76%", "rev": "$12,400", "status": "Review Needed"},
        {"name": "Perth City Center", "loc": "Perth", "occ": "82%", "rev": "$18,900", "status": "Clean Data"},
        {"name": "Brisbane Suites", "loc": "Brisbane", "occ": "91%", "rev": "$22,100", "status": "Mews Audit"},
    ]

    # --- کامپوننت‌ها ---
    def create_status_badge(status):
        if "Clean" in status: bg, b_col = badge_green, "green"
        elif "Sync" in status: bg, b_col = badge_orange, "orange"
        else: bg, b_col = badge_red, "red"
            
        return ft.Container(
            content=ft.Text(status, size=11, weight="bold", color="white"),
            bgcolor=bg,
            # FIX 1: استفاده از Padding کلاس با حرف بزرگ (رفع Deprecation)
            padding=ft.Padding(10, 5, 10, 5), 
            border_radius=15,
            # FIX 2: استفاده از Border کلاس با حرف بزرگ (رفع Deprecation)
            border=ft.Border.all(1, b_col)
        )

    def create_kpi_card(title, value, subtext, icon, trend_up=True):
        return ft.Container(
            content=ft.Row([
                ft.Container(
                    content=ft.Icon(icon, color=accent_color if trend_up else "red", size=28),
                    bgcolor="#33000000", padding=12, border_radius=12
                ),
                ft.Column([
                    ft.Text(title, size=12, color=text_muted, weight="w500"),
                    ft.Text(value, size=22, weight="bold", color="white"),
                    ft.Row([
                        ft.Icon("trending_up" if trend_up else "trending_down",
                               color="green" if trend_up else "red", size=14),
                        ft.Text(subtext, size=11, color="green" if trend_up else "red")
                    ], spacing=2)
                ], spacing=2)
            ], spacing=15),
            bgcolor=card_glass,
            padding=15, border_radius=15, expand=True,
            border=ft.Border.all(1, border_color)
        )

    def create_mini_chart(label, value_height):
        return ft.Column([
            ft.Container(width=20, height=value_height, bgcolor=accent_color, border_radius=3),
            ft.Text(label, size=10)
        ], horizontal_alignment="center")

    # --- محتوای اصلی ---
    def get_overview_content():
        rows = []
        for p in properties_data:
            rev_num = float(p['rev'].replace('$', '').replace(',', ''))
            revpar = rev_num / 100
            rows.append(
                ft.DataRow(cells=[
                    ft.DataCell(ft.Row([ft.Icon("apartment", size=16, color=text_muted), ft.Text(p['name'], weight="bold")])),
                    ft.DataCell(ft.Text(p['loc'])),
                    ft.DataCell(ft.Text(p['occ'])),
                    ft.DataCell(ft.Text(p['rev'])),
                    ft.DataCell(ft.Text(f"${revpar:.1f}", color=accent_color, weight="bold")),
                    ft.DataCell(create_status_badge(p['status'])),
                ])
            )
            
        return ft.Column([
            ft.Text("Portfolio Overview", size=22, weight="bold"),
            ft.Divider(height=10, color="transparent"),
            
            ft.Row([
                create_kpi_card("Total Revenue", "$169,700", "Daily Aggr.", "attach_money"),
                create_kpi_card("Occupancy", "87.7%", "+2% vs L.W.", "hotel"),
                create_kpi_card("System Health", "98%", "Stable", "dns"),
            ], spacing=20, wrap=True),
            
            ft.Divider(height=20, color="transparent"),
            ft.Text("Weekly Revenue Trend", size=14, color=text_muted),
            
            ft.Row([
                create_mini_chart("Mon", 40), create_mini_chart("Tue", 70),
                create_mini_chart("Wed", 50), create_mini_chart("Thu", 90),
                create_mini_chart("Fri", 100)
            ], spacing=20, scroll="auto"),
            
            ft.Divider(height=20, color="transparent"),
            
            # FIX 3: اسکرول را به Row دادیم و از کانتینر حذف کردیم
            ft.Container(
                content=ft.Row(
                    [
                        ft.DataTable(
                            columns=[
                                ft.DataColumn(ft.Text("PROPERTY")),
                                ft.DataColumn(ft.Text("LOC")),
                                ft.DataColumn(ft.Text("OCC")),
                                ft.DataColumn(ft.Text("REV")),
                                ft.DataColumn(ft.Text("RevPAR", color=accent_color)),
                                ft.DataColumn(ft.Text("STATUS")),
                            ],
                            rows=rows,
                            heading_row_height=40,
                            data_row_min_height=55,
                            vertical_lines=ft.border.BorderSide(0, "transparent"),
                            horizontal_lines=ft.border.BorderSide(1, "#1AFFFFFF"),
                            column_spacing=20
                        )
                    ],
                    scroll="auto" # اسکرول صحیح اینجاست
                ),
                bgcolor=card_glass, 
                border_radius=15, 
                padding=20,
                border=ft.Border.all(1, border_color)
            )
        ], scroll="auto", expand=True)

    def get_framework_content():
        return ft.Column([
            ft.Text("System Architecture", size=22, weight="bold"),
            ft.Divider(height=20, color="transparent"),
            ft.Container(
                content=ft.Row([
                    ft.Column([ft.Icon("input", color="cyan"), ft.Text("Raw Data")]),
                    ft.Icon("arrow_forward", color=text_muted),
                    ft.Column([ft.Icon("memory", color="cyan"), ft.Text("Processing")]),
                    ft.Icon("arrow_forward", color=text_muted),
                    ft.Column([ft.Icon("dashboard", color="cyan"), ft.Text("Dashboard")]),
                ], alignment="center", spacing=20, wrap=True),
                bgcolor="#1AFFFFFF", padding=20, border_radius=15,
                border=ft.Border.all(1, border_color)
            )
        ], expand=True)

    # --- چیدمان صفحه ---
    content_area = ft.Container(content=get_overview_content(), expand=True, padding=20)

    def change_view(e):
        idx = e.control.selected_index
        if idx == 0: content_area.content = get_overview_content()
        elif idx == 1: content_area.content = get_framework_content()
        page.update()

    sidebar = ft.NavigationRail(
        selected_index=0,
        label_type="all",
        min_width=100,
        bgcolor="#CC08090C",
        destinations=[
            ft.NavigationRailDestination(icon="dashboard", label="Overview"),
            ft.NavigationRailDestination(icon="settings", label="System"),
        ],
        on_change=change_view
    )

    # FIX 4: استفاده از "cover" به عنوان رشته متنی (جلوگیری از ارور ImageFit)
    page.add(
        ft.Stack([
            ft.Image(
                src="https://images.unsplash.com/photo-1542314831-068cd1dbfeeb",
                width=1400, height=950,
                fit="cover", # <--- تغییر مهم: استفاده از String
                opacity=0.4
            ),
            ft.Container(gradient=ft.LinearGradient(colors=["#CC000000", "#E6101216"]), expand=True),
            ft.Row([sidebar, ft.VerticalDivider(width=1, color="#1AFFFFFF"), content_area], expand=True)
        ], expand=True)
    )

if __name__ == "__main__":
    ft.app(target=main)
