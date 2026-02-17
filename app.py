import flet as ft

def main(page: ft.Page):
    # --- 1. تنظیمات صفحه ---
    page.title = "Hotel Dashboard"
    page.theme_mode = "dark"
    page.bgcolor = "black"
    page.padding = 30
    page.scroll = "auto" # اسکرول صفحه روشن

    # --- 2. استایل‌های ساده و امن ---
    card_bg = "#1A1A1A"
    text_color = "white"

    # --- 3. ساخت کارت‌های ساده (با سایز مشخص برای جلوگیری از ارور) ---
    def simple_card(title, val, color_code):
        return ft.Container(
            content=ft.Column([
                ft.Text(title, size=12, color="grey"),
                ft.Text(val, size=24, weight="bold", color="white"),
                ft.Container(height=5, width=50, bgcolor=color_code, border_radius=5)
            ]),
            bgcolor=card_bg,
            padding=20,
            border_radius=10,
            width=200,  # عرض ثابت دادیم که گیج نشود
            height=120, # ارتفاع ثابت دادیم که باکس خاکستری نشود
        )

    # --- 4. ساخت جدول (بدون کانتینرهای اضافی) ---
    # داده‌ها
    data = [
        ["St Kilda", "Melb", "94%", "$24,500"],
        ["Sydney View", "Syd", "88%", "$31,200"],
        ["Gold Coast", "GC", "98%", "$45,000"],
        ["Adelaide", "Adl", "76%", "$12,400"],
        ["Brisbane", "Bri", "91%", "$22,100"],
    ]

    # ردیف‌ها
    my_rows = []
    for item in data:
        my_rows.append(ft.DataRow(cells=[
            ft.DataCell(ft.Text(item[0], weight="bold")),
            ft.DataCell(ft.Text(item[1])),
            ft.DataCell(ft.Text(item[2], color="green")),
            ft.DataCell(ft.Text(item[3])),
        ]))

    # خودِ جدول
    my_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("HOTEL")),
            ft.DataColumn(ft.Text("LOC")),
            ft.DataColumn(ft.Text("OCC")),
            ft.DataColumn(ft.Text("REV")),
        ],
        rows=my_rows,
        border=ft.Border.all(1, "#333333"),
        heading_row_color="#222222",
    )

    # --- 5. چیدمان نهایی (بسیار ساده) ---
    page.add(
        # تیتر
        ft.Text("Executive Dashboard", size=35, weight="bold", color="white"),
        ft.Text("Real-time Hotel Data", color="grey"),
        ft.Divider(height=30, color="transparent"),

        # کارت‌ها (در یک ردیف که اگر جا نبود می‌رود خط بعد)
        ft.Row([
            simple_card("REVENUE", "$169k", "cyan"),
            simple_card("OCCUPANCY", "88%", "green"),
            simple_card("HEALTH", "OK", "orange"),
        ], wrap=True, spacing=20),

        ft.Divider(height=30, color="transparent"),

        # جدول (داخل یک Row با اسکرول افقی برای امنیت)
        ft.Text("Performance Report", size=20, weight="bold"),
        ft.Row(
            [my_table],
            scroll="always" # اگر جدول بزرگ بود، اسکرول افقی بخورد
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
