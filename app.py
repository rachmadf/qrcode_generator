import os

from flask import Flask, render_template, request

from qrcode_generator import generate_qr_code


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    qr_filename = None
    error = None

    data_value = ""
    filename_value = "qrcode"

    if request.method == "POST":
        data_value = request.form.get("data", "")
        filename_value = request.form.get("filename", "").strip() or "qrcode"

        output_dir = os.path.join(
            app.root_path,
            "static",
            "generated",
        )

        try:
            output_path = generate_qr_code(
                data=data_value,
                filename=filename_value,
                output_dir=output_dir,
            )

            # Use the actual generated filename.
            qr_filename = os.path.basename(output_path)

            # Keep the .png extension out of the editable field
            # because the UI displays it separately.
            if filename_value.lower().endswith(".png"):
                filename_value = filename_value[:-4]

        except ValueError as exc:
            error = str(exc)

    return render_template(
        "index.html",
        qr_filename=qr_filename,
        error=error,
        data_value=data_value,
        filename_value=filename_value,
    )


if __name__ == "__main__":
    app.run(debug=True)