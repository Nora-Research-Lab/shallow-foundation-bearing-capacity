import gradio as gr
from shallow_foundation_bearing_capacity import compute_bearing_capacity, classify_soil

def bearing_capacity_ui(c, phi, gamma, B, Df, Dw, FS):
    try:
        result = compute_bearing_capacity(c, phi, gamma, B, Df, Dw, FS)
        if "error" in result:
            return "", "", "", "", result["error"]
        Nc = round(result["Nc"], 3)
        Nq = round(result["Nq"], 3)
        Ng = round(result["Ng"], 3)
        qu = round(result["qu"], 1)
        qa = round(result["qa"], 1)
        soil = classify_soil(phi)
        table_data = [[Nc, Nq, Ng]]
        return table_data, qu, qa, soil, ""
    except Exception as e:
        return "", "", "", "", f"Error: {str(e)}"

with gr.Blocks(title="Shallow Foundation Bearing Capacity") as demo:
    gr.Markdown("# Shallow Foundation Bearing Capacity (Terzaghi)")
    with gr.Row():
        with gr.Column():
            c = gr.Number(label="Cohesion c (kPa)", value=0.0, minimum=0)
            phi = gr.Number(label="Friction Angle φ (degrees)", value=30.0, minimum=0, maximum=90)
            gamma = gr.Number(label="Unit Weight γ (kN/m³)", value=18.0, minimum=0)
            B = gr.Number(label="Foundation Width B (m)", value=1.0, minimum=0.1)
            Df = gr.Number(label="Foundation Depth Df (m)", value=1.0, minimum=0)
            Dw = gr.Number(label="Depth to Water Table Dw (m) (0 = no water table)", value=0.0, minimum=0)
            FS = gr.Number(label="Factor of Safety FS", value=3.0, minimum=1.0)
        with gr.Column():
            table_out = gr.Dataframe(label="Bearing Capacity Factors", headers=["Nc", "Nq", "Nγ"], row_count=1, col_count=3, type="array")
            qu_out = gr.Textbox(label="Ultimate Bearing Capacity qu (kPa)")
            qa_out = gr.Textbox(label="Allowable Bearing Capacity qa (kPa)")
            soil_out = gr.Textbox(label="Soil Classification")
            error_out = gr.Textbox(label="Status / Errors", interactive=False)

    inputs = [c, phi, gamma, B, Df, Dw, FS]
    outputs = [table_out, qu_out, qa_out, soil_out, error_out]
    for inp in inputs:
        inp.change(fn=bearing_capacity_ui, inputs=inputs, outputs=outputs)
    demo.load(fn=bearing_capacity_ui, inputs=inputs, outputs=outputs)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
