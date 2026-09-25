import math

def bearing_capacity_factors(phi_deg):
    phi_rad = math.radians(phi_deg)
    tan_phi = math.tan(phi_rad)
    if phi_deg == 0:
        Nc = 5.14
        Nq = 1.0
        Ng = 0.0
    else:
        Nq = math.exp(math.pi * tan_phi) * (math.tan(math.radians(45 + phi_deg / 2)) ** 2)
        Nc = (Nq - 1) / tan_phi
        Ng = 2 * (Nq + 1) * tan_phi
    return Nc, Nq, Ng

def effective_unit_weight(gamma, B, Df, Dw):
    if Dw <= 0:
        return gamma
    depth = B + Df
    if Dw >= depth:
        return gamma
    gamma_water = 9.81
    ratio = Dw / depth
    gamma_eff = gamma * ratio + (gamma - gamma_water) * (1 - ratio)
    return gamma_eff

def compute_bearing_capacity(c, phi_deg, gamma, B, Df, Dw, FS):
    # Input validation
    if any(v < 0 for v in [c, phi_deg, gamma, B, Df, Dw, FS]):
        return {"error": "All inputs must be non-negative."}
    if B <= 0 or Df < 0:
        return {"error": "Foundation width B must be positive; Df >= 0."}
    if FS <= 0:
        return {"error": "Factor of safety must be positive."}
    if phi_deg > 90:
        return {"error": "Friction angle cannot exceed 90 degrees."}

    Nc, Nq, Ng = bearing_capacity_factors(phi_deg)
    gamma_eff = effective_unit_weight(gamma, B, Df, Dw)
    qu = c * Nc + gamma_eff * Df * Nq + 0.5 * gamma_eff * B * Ng
    qa = qu / FS
    return {"Nc": Nc, "Nq": Nq, "Ng": Ng, "qu": qu, "qa": qa}

def classify_soil(phi_deg):
    if phi_deg < 5:
        return "Very soft clay"
    elif phi_deg < 10:
        return "Soft clay"
    elif phi_deg < 20:
        return "Stiff clay"
    elif phi_deg < 30:
        return "Dense sand"
    elif phi_deg < 40:
        return "Very dense sand"
    else:
        return "Gravel/sand"
