# Power BI Dashboard Guide (Beginner Steps)

> **Note:** A Power BI file (`.pbix`) can only be created and saved using the actual
> Power BI Desktop application on your computer — it's not a file type that can be
> generated outside of it. This guide walks you through building the dashboard
> yourself in about 20-30 minutes using the same `retail_sales_data.csv` file from
> the `data` folder. Once you save it, you'll have a real `Sales_Dashboard.pbix`
> file to show off.

## Step 1: Install Power BI Desktop
Download it for free from: https://powerbi.microsoft.com/desktop/
(Windows only. If you're on Mac, use Power BI Service in browser, or a Windows VM.)

## Step 2: Load the Data
1. Open Power BI Desktop
2. Click **Home > Get Data > Text/CSV**
3. Select `data/retail_sales_data.csv`
4. Click **Load** (not "Transform Data" — we don't need to change anything for this project)

## Step 3: Create Simple Measures (basic DAX — copy-paste these)
Go to **Modeling > New Measure** and add each of these one at a time:

```
Total Sales = SUM(retail_sales_data[Sales])

Total Profit = SUM(retail_sales_data[Profit])

Total Orders = COUNTROWS(retail_sales_data)

Average Order Value = DIVIDE([Total Sales], [Total Orders])

Profit Margin % = DIVIDE([Total Profit], [Total Sales])
```

> Don't worry about fully understanding DAX syntax yet — just know that a
> "measure" is a calculation, similar to writing a formula in Excel. Being able
> to say "I created DAX measures like SUM and DIVIDE" is a great line for your
> resume/interview.

## Step 4: Build the Report Page
Add these visuals by dragging fields from the right-hand panel onto the canvas:

1. **Card visuals** (top row) — one each for:
   - Total Sales
   - Total Profit
   - Total Orders
   - Average Order Value

2. **Bar chart** — "Total Sales by Region"
   - Axis: `Region`
   - Values: `Total Sales`

3. **Column chart** — "Profit by Category"
   - Axis: `Category`
   - Values: `Total Profit`

4. **Line chart** — "Monthly Sales Trend"
   - Axis: `OrderDate` (set to continuous, group by Month)
   - Values: `Total Sales`

5. **Pie chart** — "Orders by Payment Mode"
   - Legend: `PaymentMode`
   - Values: `Total Orders`

6. **Table** — Top 10 Customers
   - Columns: `CustomerID`, `Total Sales`
   - Sort descending by Total Sales, then use the filter pane to keep Top 10

7. **Slicer** — add a slicer for `Region` and one for `Category` at the top
   so you can filter the whole dashboard by clicking them (this is the
   "interactive" part that's great to demo in an interview)

## Step 5: Format It
- Add a title text box: "Retail Sales Performance Dashboard – 2024"
- Pick 1-2 theme colors: **View > Themes**
- Align your visuals into a neat grid

## Step 6: Save
- File > Save As > `Sales_Dashboard.pbix`
- Keep it in this `powerbi` folder

## What to Say in an Interview About This
- "I connected Power BI to a CSV dataset of retail sales."
- "I built DAX measures for total sales, profit, profit margin, and average order value."
- "I created an interactive dashboard with slicers so users can filter by region and category."
- "I identified that [best region from your Python analysis] had the highest sales
  and [best category] had the highest profit margin."

## If You Want a Screenshot Instead
If you don't have time to build it live, at minimum take a screenshot of your
finished Power BI dashboard and save it as `powerbi/dashboard_screenshot.png`
— many resumes/portfolios include a screenshot link instead of the live file.
