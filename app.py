import os

from flask import Flask, render_template, request

from qrcode_generator import generate_qr_code


app = Flask(__name__)


DEFAULT_FOREGROUND = "#000000"
DEFAULT_BACKGROUND = "#FFFFFF"
DEFAULT_BOX_SIZE = 10
DEFAULT_BORDER = 4

MIN_BOX_SIZE = 1
MAX_BOX_SIZE = 20

MIN_BORDER = 0
MAX_BORDER = 10


@app.route("/", methods=["GET", "POST"])
def index():
    qr_filename = None
    error = None

    data_value = ""
    filename_value = "qrcode"

    foreground_color = DEFAULT_FOREGROUND
    background_color = DEFAULT_BACKGROUND
    box_size = DEFAULT_BOX_SIZE
    border = DEFAULT_BORDER

    if request.method == "POST":
        data_value = request.form.get("data", "")
        filename_value = (
            request.form.get("filename", "").strip() or "qrcode"
        )

        foreground_color = request.form.get(
            "foreground_color",
            DEFAULT_FOREGROUND,
        )

        background_color = request.form.get(
            "background_color",
            DEFAULT_BACKGROUND,
        )

        try:
            box_size = int(
                request.form.get(
                    "box_size",
                    DEFAULT_BOX_SIZE,
                )
            )

            border = int(
                request.form.get(
                    "border",
                    DEFAULT_BORDER,
                )
            )

            if not MIN_BOX_SIZE <= box_size <= MAX_BOX_SIZE:
                raise ValueError(
                    f"QR size must be between "
                    f"{MIN_BOX_SIZE} and {MAX_BOX_SIZE}."
                )

            if not MIN_BORDER <= border <= MAX_BORDER:
                raise ValueError(
                    f"Border must be between "
                    f"{MIN_BORDER} and {MAX_BORDER}."
                )

        except ValueError as exc:
            error = str(exc)

        if error is None:
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
                    box_size=box_size,
                    border=border,
                    fill_color=foreground_color,
                    back_color=background_color,
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
        foreground_color=foreground_color,
        background_color=background_color,
        box_size=box_size,
        border=border,
    )


if __name__ == "__main__":
    app.run(debug=True)