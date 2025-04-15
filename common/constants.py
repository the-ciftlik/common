MODEL_TIME_INTERVAL_SECONDS = 60 * 60 * 24 * 7  # 1 week

HECTARES = "ha"
DECARES = "da"
M2 = "m2"

DATE_COL = "Date"
DATE_FORMAT = "%Y-%m-%d"

SEED_PRICE_COL = "Seed Price"

PLANTING_LABOR_PRICE_COL = "Planting Labor Price"
MAINTENANCE_LABOR_PRICE_COL = "Maintenance Labor Price"
HARVESTING_LABOR_PRICE_COL = "Harvesting Labor Price"

MACHINERY_PRICE_COL = "Machinery Price"

# N_FERTILIZER_PRICE_COL = "Nitrogen Fertilizer Price"
# P_FERTILIZER_PRICE_COL = "Phosphorus Fertilizer Price"
# K_FERTILIZER_PRICE_COL = "Potassium Fertilizer Price"
FERTILIZER_PRICE_COL = "Fertilizer Price"

PESTICIDE_PRICE_COL = "Pesticide Price"

TRANSPORTATION_PRICE_COL = "Transportation Price"

IRRIGATION_PRICE_COL = "Irrigation Price"

MARKET_PRICE_COL = "Market Price"

# !! WEATHER FILE IS NOT IMPLEMENTED YET

# === File structures ===
SEED_FILE = {DATE_COL, SEED_PRICE_COL}
LABOR_FILE = {
    DATE_COL,
    PLANTING_LABOR_PRICE_COL,
    MAINTENANCE_LABOR_PRICE_COL,
    HARVESTING_LABOR_PRICE_COL,
}
MACHINERY_FILE = {DATE_COL, MACHINERY_PRICE_COL}
IRRIGATION_FILE = {DATE_COL, IRRIGATION_PRICE_COL}
# FERTILIZER_FILE = {
#     DATE_COL,
#     N_FERTILIZER_PRICE_COL,
#     P_FERTILIZER_PRICE_COL,
#     K_FERTILIZER_PRICE_COL,
# } # not now
FERTILIZER_FILE = {DATE_COL, FERTILIZER_PRICE_COL}
PESTICIDE_FILE = {DATE_COL, PESTICIDE_PRICE_COL}
LOGISTICS_FILE = {DATE_COL, TRANSPORTATION_PRICE_COL}
MARKET_FILE = {DATE_COL, MARKET_PRICE_COL}
WEATHER_FILE = {DATE_COL}  #!! Not implemented yet
