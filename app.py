import flet as ft


def main(page: ft.Page):

    # --- تنظیمات صفحه (استایل لوکس و اگزکتیو) ---

    page.title = "HotelOps Executive | Australian Portfolio"

    page.theme_mode = "dark"

    page.padding = 0

    page.spacing = 0

    page.window_width = 1400

    page.window_height = 950

    page.bgcolor = "#000000"



    # --- استایل‌های شیشه‌ای (Glassmorphism) ---

    glass_bg = ft.colors.with_opacity(0.7, "#101216")  

    card_glass = ft.colors.with_opacity(0.5, "#1A1D24")

    border_color = ft.colors.with_opacity(0.3, "white")

    accent_color = "cyan"

    text_muted = "#B0B3B8"



    # --- داده‌های ساختگی (Simulated Data) ---

    properties_data = [

        {"name": "The St Kilda Esplanade", "loc": "Melbourne", "occ": "94%", "rev": "$24,500", "pnl": "+12%", "status": "Clean Data"},

        {"name": "Sydney Harbour View", "loc": "Sydney", "occ": "88%", "rev": "$31,200", "pnl": "+8%", "status": "Clean Data"},

        {"name": "Gold Coast Resort", "loc": "Gold Coast", "occ": "98%", "rev": "$45,000", "pnl": "+15%", "status": "Xero Sync"},

        {"name": "Adelaide Heritage", "loc": "Adelaide", "occ": "76%", "rev": "$12,400", "pnl": "-2%", "status": "Review Needed"},

        {"name": "Perth City Center", "loc": "Perth", "occ": "82%", "rev": "$18,900", "pnl": "+5%", "status": "Clean Data"},

        {"name": "Brisbane River Suites", "loc": "Brisbane", "occ": "91%", "rev": "$22,100", "pnl": "+9%", "status": "Mews Audit"},

        {"name": "Hobart Waterfront", "loc": "Tasmania", "occ": "85%", "rev": "$15,600", "pnl": "+4%", "status": "Clean Data"},

    ]



    # --- توابع کمکی UI ---

    def create_status_badge(status):

        color = "green" if "Clean" in status else "orange" if "Sync" in status else "red"

        return ft.Container(

            content=ft.Text(status, size=11, weight="bold", color="white"),

            bgcolor=ft.colors.with_opacity(0.2, color),

            padding=ft.padding.symmetric(horizontal=10, vertical=5),

            border_radius=15,

            border=ft.border.all(1, color)

        )



    def create_kpi_card(title, value, subtext, icon, trend_up=True):

        return ft.Container(

            content=ft.Row([

                ft.Container(

                    content=ft.Icon(icon, color=accent_color if trend_up else "red", size=28),

                    bgcolor=ft.colors.with_opacity(0.2, "black"), padding=12, border_radius=12

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

            padding=15,

            border_radius=15,

            expand=True,

            border=ft.border.all(1, border_color),

            blur=ft.Blur(10, 10, ft.BlurTileMode.MIRROR)

        )



    # --- صفحات مختلف (Views) ---

   

    # 1. صفحه Overview

        # یک نمودار میله‌ای ساده با استفاده از کانتینرها (برای اطمینان از رندر شدن)
    def create_mini_chart(label, value_height):
        return ft.Column([
            ft.Container(width=20, height=value_height, bgcolor=accent_color, border_radius=3),
            ft.Text(label, size=10)
        ], horizontal_alignment="center")

    # 1. صفحه Overview (اصلاح شده)
    def get_overview_content():
        rows = []
        for p in properties_data:
            # محاسبات RevPAR
            rev_number = float(p['rev'].replace('$', '').replace(',', ''))
            revpar = rev_number / 100

            rows.append(
                ft.DataRow(cells=[
                    ft.DataCell(ft.Row([ft.Icon("apartment", size=16, color=text_muted), ft.Text(p['name'] , weight="bold")])),
                    ft.DataCell(ft.Text(p['loc'])),
                    ft.DataCell(ft.Text(p['occ'], color="green" if int(p['occ'].strip('%')) > 80 else "orange")),
                    ft.DataCell(ft.Text(p['rev'])),
                    # ستون جدید RevPAR
                    ft.DataCell(ft.Text(f"${revpar:.1f}", color=accent_color, weight="bold")),
                    ft.DataCell(create_status_badge(p['status'])),
                ])
            )
        
        # تعریف ردیف نمودار (اینجا ساخته می‌شود)
        chart_row = ft.Row([
            create_mini_chart("Mon", 40),
            create_mini_chart("Tue", 70),
            create_mini_chart("Wed", 50),
            create_mini_chart("Thu", 90),
            create_mini_chart("Fri", 100),
        ], alignment="center", spacing=20)

        return ft.Column([
            ft.Text("Portfolio Overview (7 Properties)", size=22, weight="bold"),
            ft.Divider(color="transparent", height=10),
            ft.Row([
                create_kpi_card("Total Revenue (AUD)", "$169,700", "Daily Aggr.", "attach_money"),
                create_kpi_card("Avg. Occupancy", "87.7%", "+2% vs Last Wk", "hotel"),
                create_kpi_card("Data Health", "98%", "Formulas Optimized", "dns"),
            ], spacing=20),
            
            ft.Divider(color="transparent", height=20),
            
            # --- تغییر اصلی اینجاست: اضافه کردن نمودار به صفحه ---
            ft.Text("Weekly Revenue Trend", size=14, color=text_muted),
            chart_row, 
            ft.Divider(color="transparent", height=20),
            # ---------------------------------------------------

            ft.Container(
                content=ft.DataTable(
                    columns=[
                        ft.DataColumn(ft.Text("PROPERTY")),
                        ft.DataColumn(ft.Text("LOCATION")),
                        ft.DataColumn(ft.Text("OCC %"), numeric=True),
                        ft.DataColumn(ft.Text("DAILY REV"), numeric=True),
                        # هدر ستون RevPAR
                        ft.DataColumn(ft.Text("RevPAR", color=accent_color)), 
                        ft.DataColumn(ft.Text("DATA INTEGRITY")),
                    ],
                    rows=rows,
                    heading_row_height=40,
                    data_row_min_height=55,
                    vertical_lines=ft.border.BorderSide(0, "transparent"),
                    horizontal_lines=ft.border.BorderSide(1, ft.colors.with_opacity(0.1, "white")),
                    column_spacing=20
                ),
                bgcolor=card_glass, border_radius=15, padding=20, border=ft.border.all(1, border_color)
            )
        ], scroll="auto", expand=True)



    # 2. صفحه P&L

    def get_pnl_content():

        return ft.Column([

            ft.Row([

                ft.Text("P&L Framework (Xero Integration)", size=22, weight="bold"),

                ft.FilledButton("Sync Xero", icon="sync", style=ft.ButtonStyle(bgcolor="green"))

            ], alignment="spaceBetween"),

            ft.Divider(color="transparent", height=10),

            ft.Container(

                content=ft.Column([

                    ft.Text("Consolidated Profit & Loss - AUD", weight="bold", size=16),

                    ft.Divider(color="white", opacity=0.1),

                    ft.Row([ft.Text("Total Revenue"), ft.Text("$1,240,000", weight="bold")], alignment="spaceBetween"),

                    ft.Row([ft.Text("COGS (Food & Bev)"), ft.Text("($320,000)", color="red")], alignment="spaceBetween"),

                    ft.Row([ft.Text("Labor Costs (Mews)"), ft.Text("($410,000)", color="red")], alignment="spaceBetween"),

                    ft.Divider(color="white", opacity=0.1),

                    ft.Row([ft.Text("Net Operating Profit", size=18, color=accent_color), ft.Text("$510,000", size=18, weight="bold", color=accent_color)], alignment="spaceBetween"),

                ], spacing=15),

                bgcolor=card_glass, padding=30, border_radius=15, border=ft.border.all(1, border_color), width=600

            ),

            ft.Divider(color="transparent", height=20),

            ft.Text("Formula Logic Validation:", color=text_muted),

            ft.Text("✅ ARRAYFORMULA applied to all 7 property sheets.", color="green", size=12),

            ft.Text("✅ ImportRange calls optimized for speed.", color="green", size=12),

        ], expand=True)



    # 3. صفحه Daily Ops

    def get_ops_content():

        return ft.Column([

            ft.Text("Daily Operations Logic Review", size=22, weight="bold"),

            ft.Container(

                content=ft.Column([

                    ft.ListTile(leading=ft.Icon("check_circle", color="green"), title=ft.Text("Morning Audit"), subtitle=ft.Text("Mews & Cloudbeds data matched successfully.")),

                    ft.ListTile(leading=ft.Icon("warning", color="orange"), title=ft.Text("Housekeeping Discrepancy"), subtitle=ft.Text("Adelaide property shows -2 rooms variance.")),

                    ft.ListTile(leading=ft.Icon("check_circle", color="green"), title=ft.Text("Rate Parity Check"), subtitle=ft.Text("All channels synced via SiteMinder.")),

                ]),

                bgcolor=card_glass, border_radius=15, padding=10

            )

        ])



    # 4. صفحه Framework (صفحه جدید و مهم!)

    def get_framework_content():

        pipeline = ft.Container(
            content=ft.Row([
                ft.Column([ft.Icon("input", color="cyan"), ft.Text("Raw Data")]),
                ft.Icon("arrow_forward", color=text_muted),
                ft.Column([ft.Icon("memory", color="cyan"), ft.Text("Python Core")]),
                ft.Icon("arrow_forward", color=text_muted),
                ft.Column([ft.Icon("dashboard", color="cyan"), ft.Text("Executive UI")]),
            ], alignment="center", spacing=30),
            bgcolor=ft.colors.with_opacity(0.1, "white"),
            padding=20,
            border_radius=15,
            border=ft.border.all(1, border_color)
        )

        return ft.Column([

            ft.Text("System Architecture & Optimizations", size=22, weight="bold"),

            ft.Divider(height=10, color="transparent"),
            pipeline,

            ft.Text("Review of Data Flow & Formula Integrity", size=14, color=text_muted),

            ft.Divider(color="transparent", height=20),

           

            ft.Row([

                # کارت وضعیت اتصال‌ها

                ft.Container(

                    content=ft.Column([

                        ft.Text("Data Sources", weight="bold"),

                        ft.Divider(color="white", opacity=0.1),

                        ft.ListTile(leading=ft.Icon("check", color="green"), title=ft.Text("Xero API"), subtitle=ft.Text("Connected (Last sync: 2 min ago)")),

                        ft.ListTile(leading=ft.Icon("check", color="green"), title=ft.Text("Mews PMS"), subtitle=ft.Text("Connected (Live)")),

                        ft.ListTile(leading=ft.Icon("sync", color="orange"), title=ft.Text("Cloudbeds"), subtitle=ft.Text("Syncing...")),

                        ft.ListTile(leading=ft.Icon("table_chart", color="blue"), title=ft.Text("Google Sheets"), subtitle=ft.Text("Master Sheet Operational")),

                    ]),

                    bgcolor=card_glass, border_radius=15, padding=20, expand=True, border=ft.border.all(1, border_color)

                ),

                # کارت بهینه‌سازی‌ها (نشان‌دهنده تخصص تو)

                ft.Container(

                    content=ft.Column([

                        ft.Text("Formula & Structure Audit", weight="bold"),

                        ft.Divider(color="white", opacity=0.1),

                        ft.ListTile(leading=ft.Icon("build", color="cyan"), title=ft.Text("Logic Tightening"), subtitle=ft.Text("Nested IFERRORs implemented to prevent #N/A.")),

                        ft.ListTile(leading=ft.Icon("speed", color="cyan"), title=ft.Text("Speed Optimization"), subtitle=ft.Text("Reduced volatile functions (TODAY/NOW).")),

                        ft.ListTile(leading=ft.Icon("send", color="purple"), title=ft.Text("Auto-Reporting"), subtitle=ft.Text("Scheduled daily PDF export to Head Office.")),

                    ]),

                    bgcolor=card_glass, border_radius=15, padding=20, expand=True, border=ft.border.all(1, border_color)

                )

            ], expand=True, spacing=20)

        ], expand=True)



    # --- کانتینر اصلی محتوا ---

    content_area = ft.Container(content=get_overview_content(), expand=True, padding=30)



    # --- مدیریت رویدادها ---

    def change_view(e):

        idx = e.control.selected_index

        # منطق تعویض صفحات (با اضافه شدن ایندکس 3)

        if idx == 0:

            content_area.content = get_overview_content()

        elif idx == 1:

            content_area.content = get_pnl_content()

        elif idx == 2:

            content_area.content = get_ops_content()

        elif idx == 3: # بخش فریمورک که اضافه شد

            content_area.content = get_framework_content()

       

        page.update()



    def show_notifications(e):

        page.show_dialog(

            ft.AlertDialog(

                title=ft.Text("System Alerts"),

                content=ft.Column([

                    ft.Text("• Formulas updated for St Kilda Sheet"),

                    ft.Text("• Xero Token refreshed"),

                    ft.Text("• Daily Report sent to Head Office"),

                ], height=100),

            )

        )



    # --- ساختار کلی صفحه ---

    sidebar = ft.NavigationRail(

        selected_index=0,

        label_type="all",

        min_width=100,

        bgcolor=ft.colors.with_opacity(0.8, "#08090C"),

        group_alignment=-0.9,

        destinations=[

            ft.NavigationRailDestination(icon="dashboard", label="Overview"),

            ft.NavigationRailDestination(icon="pie_chart", label="P&L Reports"),

            ft.NavigationRailDestination(icon="list_alt", label="Daily Ops"),

            ft.NavigationRailDestination(icon="settings", label="Framework"), # دکمه فریمورک

        ],

        on_change=change_view

    )



    header = ft.Row([

        ft.Column([

            ft.Text("HotelOps Framework", size=20, weight="bold", color="white"),

            ft.Text("Exec-Ready Reporting | Australia", size=12, color=text_muted)

        ], spacing=2),

        ft.Row([

            ft.IconButton("notifications", icon_color="white", on_click=show_notifications, tooltip="Alerts"),

            ft.Container(

                content=ft.Row([

                    ft.CircleAvatar(foreground_image_url="https://ui-avatars.com/api/?name=GM&background=0D8ABC&color=fff", radius=18),

                    ft.Column([ft.Text("General Manager", size=12, weight="bold"), ft.Text("Head Office", size=10, color=text_muted)], spacing=0)

                ]),

                bgcolor=ft.colors.with_opacity(0.1, "white"), padding=5, border_radius=25

            )

        ], spacing=15)

    ], alignment="spaceBetween")



    page.add(

        ft.Stack(

            [

                # لایه 1: تصویر پس‌زمینه

                ft.Image(

                    src="https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?q=80&w=2070&auto=format&fit=crop",

                    width=1400, height=950, fit=ft.ImageFit.COVER, opacity=0.4

                ),

                # لایه 2: گرادینت تیره

                ft.Container(

                    gradient=ft.LinearGradient(

                        begin=ft.alignment.top_center, end=ft.alignment.bottom_center,

                        colors=[ft.colors.with_opacity(0.8, "#000000"), ft.colors.with_opacity(0.9, "#101216")]

                    ),

                    expand=True

                ),

                # لایه 3: محتوا

                ft.Row(

                    [

                        sidebar,

                        ft.VerticalDivider(width=1, color=ft.colors.with_opacity(0.1, "white")),

                        ft.Container(

                            content=ft.Column([header, ft.Divider(color="transparent"), content_area], expand=True),

                            expand=True, padding=20

                        )

                    ],

                    expand=True, spacing=0

                )

            ],

            expand=True

        )

    )



ft.app(target=main)
