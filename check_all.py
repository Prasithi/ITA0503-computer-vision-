import subprocess
import sys
from pathlib import Path

folder = Path(__file__).parent
report = []

print("\n========== COMPUTER VISION LAB DIAGNOSTIC ==========\n")

for number in range(1, 41):
    file = folder / f"experiment{number}.py"

    if not file.exists():
        report.append(f"Experiment {number}: FILE MISSING")
        print(f"[MISSING] Experiment {number}")
        continue

    try:
        result = subprocess.run(
            [sys.executable, str(file)],
            capture_output=True,
            text=True,
            input="",
            timeout=12,
            cwd=folder
        )

        output = (result.stdout + "\n" + result.stderr).strip()

        if result.returncode == 0:
            status = "PASSED"
        elif "EOFError" in output:
            status = "INPUT REQUIRED"
        else:
            status = "ERROR"

        report.append(
            f"\n===== Experiment {number}: {status} =====\n{output}"
        )
        print(f"[{status}] Experiment {number}")

    except subprocess.TimeoutExpired:
        report.append(
            f"\n===== Experiment {number}: TIMEOUT =====\n"
            "May be waiting for a key press, GUI window, or input."
        )
        print(f"[TIMEOUT] Experiment {number}")

    except Exception as error:
        report.append(
            f"\n===== Experiment {number}: FAILED =====\n{error}"
        )
        print(f"[FAILED] Experiment {number}")

report_path = folder / "diagnostic_report.txt"
report_path.write_text("\n".join(report), encoding="utf-8")

print("\n========== DIAGNOSTIC COMPLETED ==========")
print(f"Report saved at: {report_path}")
