import pandas as pd


df = pd.DataFrame(
    {
        "total_points":
            [
                "Menos de 7 puntos",
                "De 7 a 11 puntos",
                "De 12 a 14 puntos",
                "De 15 a 20 puntos",
                "Más de 20 puntos"
            ],
        "risk_diabetes": [
            "1%",
            "4%",
            "17%",
            "33%",
            "50%"
        ],
        "interpretation": [
            "Nivel de riesgo bajo",
            "Nivel de riesgo ligeramente elevado",
            "Nivel de riesgo moderado",
            "Nivel de riesgo alto",
            "Nivel de riesgo muy alto"
        ]
    }
)