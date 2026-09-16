import os

from flask import Flask, render_template, request

from qrcode_generator import generate_qr_code


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    qr_filename = None
    error = None

    if request.method == "POST":
        data = request.form.get("data", "")
        filename = request.form.get("filename", "").strip() or "qrcode"

        output_dir = os.path.join(
            app.root_path,
            "static",
            "generated",
        )

        try:
            generate_qr_code(
                data=data,
                filename=filename,
                output_dir=output_dir,
            )

            # Filename is already validated and normalized
            # by generate_qr_code().
            if not filename.lower().endswith(".png"):
                filename += ".png"

            qr_filename = filename

        except ValueError as exc:
            error = str(exc)

    return render_template(
        "index.html",
        qr_filename=qr_filename,
        error=error,
    )


if __name__ == "__main__":
    app.run(debug=True)