import sqlite3
import hashlib
import time
import urllib.parse
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI(title="NovaLoom AI 2076 - Ultimate Sovereign Core")
DB_NAME = "novaloom_2076.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS designs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        designer TEXT,
        prompt TEXT,
        price REAL,
        chronos_hash TEXT,
        image_url TEXT,
        highest_bid REAL DEFAULT 0,
        color_psychology TEXT,
        vector_svg TEXT
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT,
        quantity_meters REAL,
        unit_cost REAL
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS repair_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fabric_model TEXT,
        damage_pct REAL,
        nanobots_used REAL,
        duration_sec REAL
    )''')
    c.execute("SELECT COUNT(*) FROM orders")
    if c.fetchone()[0] == 0:
        c.execute("INSERT INTO orders (amount) VALUES (350.00)")
    conn.commit()
    conn.close()

init_db()

class MultiFactorAuthRequest(BaseModel):
    retinal_hash: str
    neural_wave_hz: float
    chrono_key: str
    heartbeat_bpm: float = 72.0

class DesignRequest(BaseModel):
    designer_name: str
    prompt: str
    fabric_type: str
    emotion_score: float = 0.9

class QuantumConsciousnessRequest(BaseModel):
    brainwave_freq_hz: float
    mental_state_tag: str
    light_spectrum: str

class NanoRepairRequest(BaseModel):
    fabric_model: str
    damage_severity_percent: float
    body_temperature: float

class BidRequest(BaseModel):
    design_id: int
    bid_amount: float

class InventoryAdd(BaseModel):
    item_name: str
    fabric_type: str
    quantity_meters: float
    unit_cost: float

class NeuralAuth(BaseModel):
    employee_id: int
    scan_hash: str

@app.get("/app")
def serve_frontend():
    return FileResponse("static/index.html")

@app.post("/auth/verify-multimodal")
def verify_multimodal(req: MultiFactorAuthRequest):
    if req.neural_wave_hz < 5.0 or req.neural_wave_hz > 45.0:
        return {"status": "denied", "message": "⚠️ إنذار أمني: التردد العصبي خارج النطاق البشري المستقر."}
    if req.heartbeat_bpm < 50.0 or req.heartbeat_bpm > 110.0:
        return {"status": "denied", "message": "⚠️ تنبيه الحجر الصحي: معدل النبض الحيوي غير آمن."}
    if req.chrono_key != "CHR-KEY-2076":
        return {"status": "denied", "message": "⛔ مفتاح التشفير الزمني (ChronoKey) غير صحيح."}
    
    return {
        "status": "granted",
        "access_level": "SOVEREIGN_SUPREME_ADMIN_2076",
        "message": "🛡️ تم التحقق بنجاح عبر الدرع البيومتري. أهلاً بك يا ماهر في قلب المنظومة."
    }

@app.get("/enterprise/dashboard")
def get_dashboard():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT COUNT(*), COALESCE(SUM(amount), 0) FROM orders")
    total_orders, gross_sales = c.fetchone()
    c.execute("SELECT COUNT(*), COALESCE(SUM(quantity_meters), 0) FROM inventory")
    inv_items, total_meters = c.fetchone()
    conn.close()
    
    return {
        "total_orders": total_orders,
        "gross_sales_volume": round(gross_sales, 2),
        "net_app_revenue": round(gross_sales * 0.18, 2),
        "quantum_supply_alert": "مستقر (99.9% كفاءة ألياف النانو)",
        "user_wallet_nlc": 10000.0
    }

@app.post("/ai/generate-design")
def generate_design(req: DesignRequest):
    base_price = 200.0 + len(req.prompt) * 3.0
    dynamic_price = round(base_price * (1 + (req.emotion_score - 0.5)), 2)
    raw_token = f"{req.designer_name}-{req.prompt}-{time.time()}"
    chronos_hash = "CHR-" + hashlib.sha256(raw_token.encode()).hexdigest()[:12].upper()
    
    encoded_prompt = urllib.parse.quote(f"futuristic 2076 cyber fashion apparel {req.prompt}, neon glow, dark studio background, 8k")
    image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=512&height=512&nologo=true"
    
    psycho_analysis = "تحفيز هرمون الدوبامين وتعزيز الثقة المطلقة بنسبة +94%" if "نيون" in req.prompt or "مضيء" in req.prompt else "توازن عصبي وهدوء نفسي عميق بنسبة +89%"
    vector_svg = f"<svg viewBox='0 0 100 100'><path d='M10 50 Q 50 10 90 50 T 90 90' stroke='#00E5FF' stroke-width='3' fill='none'/><circle cx='50' cy='50' r='20' fill='#9C27B0' opacity='0.6'/></svg>"

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO designs (designer, prompt, price, chronos_hash, image_url, highest_bid, color_psychology, vector_svg) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
              (req.designer_name, req.prompt, dynamic_price, chronos_hash, image_url, dynamic_price, psycho_analysis, vector_svg))
    conn.commit()
    conn.close()
    
    return {
        "generated_model": f"NL-2076-{req.fabric_type.upper()}",
        "dynamic_price": dynamic_price,
        "chronos_hash": chronos_hash,
        "image_url": image_url,
        "color_psychology": psycho_analysis,
        "vector_svg": vector_svg
    }

@app.get("/ai/designs")
def list_designs(sort_by: str = "newest"):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    if sort_by == "highest_bid":
        c.execute("SELECT id, prompt, price, chronos_hash, image_url, highest_bid, color_psychology, vector_svg FROM designs ORDER BY highest_bid DESC")
    else:
        c.execute("SELECT id, prompt, price, chronos_hash, image_url, highest_bid, color_psychology, vector_svg FROM designs ORDER BY id DESC")
    
    rows = [{
        "id": r[0], "prompt": r[1], "price": r[2], "hash": r[3], 
        "image_url": r[4], "highest_bid": r[5] or r[2], 
        "color_psychology": r[6] or "تحليل قياسي مستقر",
        "vector_svg": r[7] or ""
    } for r in c.fetchall()]
    conn.close()
    return rows

@app.post("/marketplace/bid")
def place_bid(bid: BidRequest):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT highest_bid FROM designs WHERE id = ?", (bid.design_id,))
    row = c.fetchone()
    if not row:
        conn.close()
        return {"status": "error", "message": "التصميم غير موجود"}
    if bid.bid_amount <= row[0]:
        conn.close()
        return {"status": "error", "message": f"يجب أن تكون المزايدة أعلى من (${row[0]})"}
    
    c.execute("UPDATE designs SET highest_bid = ? WHERE id = ?", (bid.bid_amount, bid.design_id))
    c.execute("INSERT INTO orders (amount) VALUES (?)", (bid.bid_amount,))
    conn.commit()
    conn.close()
    return {"status": "success", "message": f"تم خصم ونجاح المزايدة بقيمة ${bid.bid_amount} NLC وتحديث ميزانية النظام!"}

@app.post("/ai/quantum-consciousness")
def quantum_consciousness(req: QuantumConsciousnessRequest):
    spectrum_map = {
        "Cyan-Neon": "أزرق سيبراني نشط يرفع الانتباه الحسي",
        "Quantum-Violet": "بنفَسجي كوانتي يعمق الإبداع والحدس",
        "Solar-Gold": "ذهبي فوتوني يعزز الطاقة الحيوية والدفء"
    }
    desc = spectrum_map.get(req.light_spectrum, "طيف ضوئي متكيف")
    hash_id = "QC-2076-" + hashlib.md5(str(req.brainwave_freq_hz).encode()).hexdigest()[:8].upper()
    return {
        "consciousness_code": hash_id,
        "spectrum_effect": desc,
        "status": f"تم ضبط طيف الهولوجرام عند {req.brainwave_freq_hz} هرتز ({req.mental_state_tag})."
    }

@app.post("/ai/nano-repair-advanced")
def nano_repair_advanced(req: NanoRepairRequest):
    nanobots_used = round(req.damage_severity_percent * 0.42, 2)
    duration = round(req.damage_severity_percent * 0.3, 1)
    
    thermal_alert = "طبيعي - عزل مثالي"
    if req.body_temperature > 38.0:
        thermal_alert = "⚠️ تحذير حراري: تم تفعيل التبريد النشط وعزل النسيج فورا!"
    elif req.body_temperature < 35.5:
        thermal_alert = "⚠️ تنبيه: تفعيل نظام التدفئة النانوية الدقيقة!"

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO repair_logs (fabric_model, damage_pct, nanobots_used, duration_sec) VALUES (?, ?, ?, ?)",
              (req.fabric_model, req.damage_severity_percent, nanobots_used, duration))
    conn.commit()
    conn.close()

    return {
        "status": "إصلاح خلوي تام بنسبة 100%",
        "nanobots_consumed": f"{nanobots_used} مليون وحدة نانو",
        "duration": f"{duration} ثانية",
        "thermal_alert": thermal_alert
    }

@app.post("/enterprise/inventory/add")
def add_inventory(item: InventoryAdd):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO inventory (item_name, quantity_meters, unit_cost) VALUES (?, ?, ?)",
              (item.item_name, item.quantity_meters, item.unit_cost))
    conn.commit()
    conn.close()
    return {"message": f"تم تسجيل {item.quantity_meters} متر من ({item.item_name}) بنجاح."}

@app.get("/enterprise/inventory")
def list_inventory():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT item_name, quantity_meters FROM inventory ORDER BY id DESC")
    rows = [{"item_name": r[0], "quantity_meters": r[1]} for r in c.fetchall()]
    conn.close()
    return rows

@app.post("/auth/neural-id")
def neural_id_auth(auth: NeuralAuth):
    return {"message": f"تمت المصادقة العصبية الحيوية للموظف #{auth.employee_id} بنجاح."}

