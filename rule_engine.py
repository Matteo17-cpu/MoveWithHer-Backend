# rule_engine.py
import random

latihan = [
    {
        "id": "Seated Toe Raises",
        "nama": "Seated Toe Raises",
        "intensity": "Low",
        "classification": ["Diplegia"]
    },
    {
        "id": "Seated Air Boxing",
        "nama": "Seated Air Boxing",
        "intensity": "Low",
        "classification": ["Paraplegia"]
    },
    {
        "id": "Lying Leg Raises",
        "nama": "Lying Leg Raises",
        "intensity": ["Medium", "High"],
        "classification": ["Diplegia"]
    },
    {
        "id": "Seated Dumbell Chest Press",
        "nama": "Seated Dumbell Chest Press",
        "intensity": ["Medium", "High"],
        "classification": ["Paraplegia"]
    },
    {
        "id": "Modified Leg Raises",
        "nama": "Modified Leg Raises",
        "intensity": ["Medium", "High"],
        "classification": ["Diplegia"]
    },
    {
        "id": "Sit-Ups",
        "nama": "Sit-Ups",
        "intensity": ["High"],
        "classification": ["Paraplegia"]
    },
    {
        "id": "Modified Lying Leg Raises",
        "nama": "Modified Lying Leg Raises",
        "intensity": ["Medium", "High"],
        "classification": ["Diplegia"]
    },
    {
        "id": "Seated Hammer Curls",
        "nama": "Seated Hammer Curls",
        "intensity": ["Medium", "High"],
        "classification": ["Paraplegia"]
    },
    {
        "id": "Seated Dumbbell Overhead Triceps Extension",
        "nama": "Seated Dumbbell Overhead Triceps Extension",
        "intensity": ["Medium"],
        "classification": ["Paraplegia"]
    },
    {
        "id": "Seated Dumbbell Shrugs",
        "nama": "Seated Dumbbell Shrugs",
        "intensity": ["Low", "Medium"],
        "classification": ["Paraplegia"]
    },
    {
        "id": "Seated Bicep Curls",
        "nama": "Seated Bicep Curls",
        "intensity": ["Low", "High"],
        "classification": ["Paraplegia"]
    },
    {
        "id": "Side Stretch",
        "nama": "Side Stretch",
        "intensity": ["Low"],
        "classification": ["Paraplegia"]
    },
    {
        "id": "Seated Twists",
        "nama": "Seated Twists",
        "intensity": ["Low"],
        "classification": ["Paraplegia"]
    },
    {
        "id": "Cross Arm Stretch",
        "nama": "Cross Arm Stretch",
        "intensity": ["Low", "High"],
        "classification": ["Paraplegia"]
    },
    {
        "id": "Dumbell Upright Row",
        "nama": "Dumbell Upright Row",
        "intensity": ["Low"],
        "classification": ["Paraplegia"]
    },
    {
        "id": "Cow Face Stretch",
        "nama": "Cow Face Stretch",
        "intensity": ["Low"],
        "classification": ["Paraplegia"]
    },
    {
        "id": "Arm Circles",
        "nama": "Low",
        "intensity": ["Low"],
        "classification": ["Paraplegia"]
    },
    {
        "id": "Bicycle Kicks",
        "nama": "Bicycle Kicks",
        "intensity": ["Medium"],
        "classification": ["Diplegia"]
    },
    {
        "id": "Arm Raises",
        "nama": "Arm Raises",
        "intensity": ["Low"],
        "classification": ["Paraplegia"]
    },
    {
        "id": "Neck Rotations",
        "nama": "Neck Rotations",
        "intensity": ["Low"],
        "classification": ["Quadriplegia"]
    },
    {
        "id": "Dumbbell Front Raise",
        "nama": "Dumbell Front Raise",
        "intensity": ["Medium", "High"],
        "classification": ["Paraplegia"]
    },
    {
        "id": "Overhead Claps Stretch",
        "nama": "Overhead Claps Stretch",
        "intensity": ["Low"],
        "classification": ["Paraplegia"]
    },
    {
        "id": "Dives",
        "nama": "Dives",
        "intensity": ["Low"],
        "classification": ["Paraplegia"]
    },
        {
        "id": "Shake it Out",
        "nama": "Shake it Out",
        "intensity": ["Low"],
        "classification": ["Paraplegia"]
    },
        {
        "id": "Seated Leg Kicks",
        "nama": "Seated Leg Kicks",
        "intensity": ["Medium"],
        "classification": ["Diplegia"]
    },
        {
        "id": "Dumbbell Overhead Pass",
        "nama": "Dumbbell Overhead Pass",
        "intensity": ["Medium", "High"],
        "classification": ["Paraplegia"]
    },
        {
        "id": "Wrist Flexor Stretch",
        "nama": "Wrist Flexor Stretch",
        "intensity": ["Low"],
        "classification": ["Paraplegia"]
    },
        {
        "id": "Chin Tucks",
        "nama": "Chin Tucks",
        "intensity": ["Low"],
        "classification": ["Quadriplegia"]
    },
        {
        "id": "Side Neck Tilt",
        "nama": "Side Neck Tilt",
        "intensity": ["Low"],
        "classification": ["Quadriplegia"]
    },
        {
        "id": "Side Lateral Front Raise",
        "nama": "Side Lateral Front Raise",
        "intensity": ["Medium", "High"],
        "classification": ["Paraplegia"]
    },
        {
        "id": "Chest Stretch",
        "nama": "Chest Stretch",
        "intensity": ["Low"],
        "classification": ["Paraplegia"]
    },
]

user = {
    "id": "user_001",
    "disabilitas": "Paraplegia",
    "BPM": 98,
}

def rekomendasi_latihan(user, latihan_list):
    hasil = []
    bpm = user.get("BPM", 100)

    if bpm > 120:
        intensitas_boleh = ["Low"]
    elif 80 <= bpm <= 120:
        intensitas_boleh = ["Low", "Medium"]
    else:
        intensitas_boleh = ["Low", "Medium", "High"]

    # Mulai loop setiap latihan
    for l in latihan_list:
        # Normalisasi intensity jadi list
        intensities = l["intensity"] if isinstance(l["intensity"], list) else [l["intensity"]]

        # Filter sesuai disabilitas
        if user["disabilitas"] not in l["classification"]:
            continue   

        # Filter sesuai intensitas
        if not any(i in intensitas_boleh for i in intensities):
            continue   

        # Kalau lolos semua aturan → tambahkan
        hasil.append(l)

    random.shuffle(hasil)
    return hasil[:4]

rekomendasi = rekomendasi_latihan(user, latihan)

if rekomendasi:
    print("Latihan yang direkomendasikan:")
    for r in rekomendasi:
        intensities = r["intensity"] if isinstance(r["intensity"], list) else [r["intensity"]]
        print(f"- {r['nama']} (Intensitas: {', '.join(intensities)})")
else:
    print("Anda tidak disarankan untuk latihan hari ini.")
