from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>DMC 5 Android Launcher</title>
<style>
body {
    background: #101014;
    color: white;
    font-family: Arial, sans-serif;
    text-align: center;
    padding: 20px;
}
h1 { color: #e63946; }
.card {
    background: #202027;
    padding: 22px;
    margin: 20px auto;
    border-radius: 15px;
    max-width: 400px;
}
button, select {
    padding: 12px;
    border-radius: 8px;
    border: none;
    margin: 8px;
    font-size: 16px;
}
button {
    background: #c62828;
    color: white;
}
select {
    background: #303038;
    color: white;
}
p { color: #c7c7ce; }
</style>
</head>
<body>

<h1>DEVIL MAY CRY 5</h1>
<p>Android Compatibility Launcher</p>

<div class="card">
    <h2>Game Library</h2>
    <p>PS4 Compatibility Prototype</p>
    <button onclick="alert('No compatible emulator core connected yet.')">
        Launch Game
    </button>
</div>

<div class="card">
    <h2>Graphics Settings</h2>
    <label>Resolution</label><br>
    <select>
        <option>720p</option>
        <option>540p</option>
        <option>480p</option>
        <option>360p</option>
    </select>
    <p>Graphics backend: Vulkan</p>
    <p>Actual graphics settings require a compatible emulator.</p>
</div>

<div class="card">
    <h2>System Status</h2>
    <p>Launcher: Ready</p>
    <p>Emulator: Not connected</p>
</div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
