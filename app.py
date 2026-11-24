
from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>SoundWave | Music Streaming</title>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', sans-serif;
    background: #09090f;
    color: white;
}

/* Layout */
.layout {
    display: flex;
    min-height: 100vh;
}

/* Sidebar */
.sidebar {
    width: 240px;
    background: #11111b;
    padding: 30px 20px;
    position: fixed;
    height: 100vh;
}

.logo {
    font-size: 27px;
    font-weight: bold;
    color: #b794ff;
    margin-bottom: 45px;
}

.logo span {
    color: #fff;
}

.menu-title {
    color: #77778b;
    font-size: 12px;
    margin: 25px 0 15px;
    letter-spacing: 2px;
}

.sidebar a {
    display: block;
    padding: 13px;
    margin-bottom: 8px;
    text-decoration: none;
    color: #aaaabd;
    border-radius: 9px;
    transition: 0.3s;
}

.sidebar a:hover,
.sidebar a.active {
    background: #29213d;
    color: #c5a5ff;
}

/* Main */
.main {
    margin-left: 240px;
    width: calc(100% - 240px);
    padding: 30px 40px 110px;
}

/* Navbar */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 35px;
    gap: 20px;
}

.search {
    background: #191925;
    border: 1px solid #29293b;
    padding: 13px 20px;
    border-radius: 30px;
    color: white;
    width: 320px;
    outline: none;
}

.profile {
    background: #29213d;
    color: #d7bdff;
    padding: 10px 18px;
    border-radius: 25px;
}

/* Hero */
.hero {
    padding: 55px;
    border-radius: 22px;
    background: linear-gradient(120deg, #48217b, #9b4de0, #ed5a9d);
    margin-bottom: 40px;
    position: relative;
    overflow: hidden;
}

.hero h1 {
    font-size: 43px;
    margin-bottom: 15px;
}

.hero p {
    color: #eee0ff;
    margin-bottom: 25px;
}

.hero button {
    padding: 13px 30px;
    border: none;
    border-radius: 30px;
    background: white;
    color: #52218a;
    font-weight: bold;
    cursor: pointer;
}

/* Sections */
.section {
    margin-bottom: 40px;
}

.section-header {
    display: flex;
    justify-content: space-between;
    margin-bottom: 22px;
}

.section-header h2 {
    font-size: 23px;
}

.section-header a {
    color: #b794ff;
    text-decoration: none;
}

/* Cards */
.cards {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(175px, 1fr));
    gap: 22px;
}

.card {
    background: #151520;
    padding: 15px;
    border-radius: 15px;
    transition: 0.3s;
    cursor: pointer;
}

.card:hover {
    background: #252238;
    transform: translateY(-5px);
}

.cover {
    height: 165px;
    border-radius: 12px;
    margin-bottom: 15px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 65px;
}

.cover1 { background: linear-gradient(135deg,#ff758c,#ff7eb3); }
.cover2 { background: linear-gradient(135deg,#4776e6,#8e54e9); }
.cover3 { background: linear-gradient(135deg,#11998e,#38ef7d); }
.cover4 { background: linear-gradient(135deg,#f7971e,#ffd200); }
.cover5 { background: linear-gradient(135deg,#654ea3,#eaafc8); }
.cover6 { background: linear-gradient(135deg,#232526,#414345); }

.card h3 {
    font-size: 16px;
    margin-bottom: 6px;
}

.card p {
    color: #89899d;
    font-size: 13px;
}

/* Genres */
.genres {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 15px;
}

.genre {
    padding: 25px;
    border-radius: 13px;
    font-size: 19px;
    font-weight: bold;
    min-height: 90px;
}

.g1 { background: linear-gradient(120deg,#642b73,#c6426e); }
.g2 { background: linear-gradient(120deg,#134e5e,#71b280); }
.g3 { background: linear-gradient(120deg,#373b44,#4286f4); }
.g4 { background: linear-gradient(120deg,#c31432,#240b36); }

/* Player */
.player {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background: #181822;
    border-top: 1px solid #30303c;
    padding: 15px 30px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 10;
}

.track {
    display: flex;
    align-items: center;
    gap: 12px;
    width: 25%;
}

.track-art {
    background: linear-gradient(135deg,#9b4de0,#ed5a9d);
    width: 45px;
    height: 45px;
    border-radius: 8px;
    display: grid;
    place-items: center;
}

.track p {
    font-size: 13px;
    color: #999;
}

.controls {
    text-align: center;
}

.controls button {
    background: none;
    border: none;
    color: white;
    font-size: 25px;
    cursor: pointer;
    margin: 0 12px;
}

.play {
    background: #b794ff !important;
    color: #111 !important;
    width: 42px;
    height: 42px;
    border-radius: 50%;
}

.progress {
    width: 250px;
    height: 4px;
    background: #444;
    margin: 10px auto 0;
    border-radius: 10px;
}

.progress div {
    height: 100%;
    width: 35%;
    background: #b794ff;
    border-radius: 10px;
}

@media(max-width: 800px) {
    .sidebar {
        width: 70px;
        padding: 20px 8px;
    }

    .logo {
        font-size: 17px;
    }

    .sidebar a {
        font-size: 0;
        text-align: center;
    }

    .main {
        margin-left: 70px;
        width: calc(100% - 70px);
        padding: 20px;
    }

    .hero {
        padding: 30px 20px;
    }

    .hero h1 {
        font-size: 30px;
    }

    .search {
        width: 100%;
    }

    .navbar {
        flex-wrap: wrap;
    }

    .track {
        width: auto;
    }

    .progress {
        width: 100px;
    }
}
</style>
</head>

<body>

<div class="layout">

    <aside class="sidebar">
        <div class="logo">♫ Sound<span>Wave</span></div>

        <div class="menu-title">MENU</div>
        <a href="/" class="active">⌂ Home</a>
        <a href="#trending">♫ Trending</a>
        <a href="#genres">◈ Explore</a>
        <a href="#artists">♙ Artists</a>

        <div class="menu-title">YOUR LIBRARY</div>
        <a href="#recent">♡ Favorites</a>
        <a href="#recent">▣ Playlists</a>
        <a href="#recent">◷ Recently Played</a>
    </aside>

    <main class="main">

        <nav class="navbar">
            <input class="search" id="search"
            placeholder="Search songs, artists, albums..."
            oninput="searchMusic()">

            <div class="profile">♫ Music Lover</div>
        </nav>

        <section class="hero">
            <h1>Feel The Music.</h1>
            <p>
                Discover millions of songs. Find your rhythm.
                Make every moment unforgettable.
            </p>
            <button onclick="playSong('Feel The Music')">
                ▶ Start Listening
            </button>
        </section>

        <section class="section" id="trending">
            <div class="section-header">
                <h2>🔥 Trending Albums</h2>
                <a href="#trending">View All →</a>
            </div>

            <div class="cards">

                <div class="card" data-name="Midnight Dreams"
                onclick="playSong('Midnight Dreams')">
                    <div class="cover cover1">🌙</div>
                    <h3>Midnight Dreams</h3>
                    <p>Various Artists</p>
                </div>

                <div class="card" data-name="Purple Sky"
                onclick="playSong('Purple Sky')">
                    <div class="cover cover2">🌌</div>
                    <h3>Purple Sky</h3>
                    <p>DJ Shadow</p>
                </div>

                <div class="card" data-name="Green Energy"
                onclick="playSong('Green Energy')">
                    <div class="cover cover3">🌿</div>
                    <h3>Green Energy</h3>
                    <p>Nature Beats</p>
                </div>

                <div class="card" data-name="Golden Hour"
                onclick="playSong('Golden Hour')">
                    <div class="cover cover4">☀️</div>
                    <h3>Golden Hour</h3>
                    <p>Sunset Music</p>
                </div>

                <div class="card" data-name="Love Stories"
                onclick="playSong('Love Stories')">
                    <div class="cover cover5">💜</div>
                    <h3>Love Stories</h3>
                    <p>Romantic Hits</p>
                </div>

                <div class="card" data-name="Dark Vibes"
                onclick="playSong('Dark Vibes')">
                    <div class="cover cover6">🎧</div>
                    <h3>Dark Vibes</h3>
                    <p>Night Beats</p>
                </div>

            </div>
        </section>

        <section class="section" id="genres">
            <div class="section-header">
                <h2>Explore By Genre</h2>
            </div>

            <div class="genres">
                <div class="genre g1">🎸 Pop Music</div>
                <div class="genre g2">🎹 Classical</div>
                <div class="genre g3">🎧 Electronic</div>
                <div class="genre g4">🎤 Hip Hop</div>
            </div>
        </section>

        <section class="section" id="artists">
            <div class="section-header">
                <h2>⭐ Popular Artists</h2>
            </div>

            <div class="cards">
                <div class="card">
                    <div class="cover cover2">🎤</div>
                    <h3>Artist One</h3>
                    <p>Popular Artist</p>
                </div>

                <div class="card">
                    <div class="cover cover1">🎙️</div>
                    <h3>Artist Two</h3>
                    <p>Music Creator</p>
                </div>

                <div class="card">
                    <div class="cover cover5">🎼</div>
                    <h3>Artist Three</h3>
                    <p>Singer & Songwriter</p>
                </div>
            </div>
        </section>

        <section class="section" id="recent">
            <div class="section-header">
                <h2>Recently Played</h2>
            </div>
            <p style="color:#999">
                Select an album to see it in the music player.
            </p>
        </section>

    </main>

</div>

<!-- Music Player -->
<div class="player">

    <div class="track">
        <div class="track-art">🎵</div>
        <div>
            <h4 id="songName">Select a Song</h4>
            <p>SoundWave Playlist</p>
        </div>
    </div>

    <div class="controls">
        <button onclick="previousSong()">⏮</button>
        <button class="play" id="playBtn"
        onclick="togglePlay()">▶</button>
        <button onclick="nextSong()">⏭</button>
        <div class="progress"><div id="progressBar"></div></div>
    </div>

    <div style="color:#b794ff">♫ SoundWave</div>

</div>

<script>
const songs = [
    "Midnight Dreams",
    "Purple Sky",
    "Green Energy",
    "Golden Hour",
    "Love Stories",
    "Dark Vibes"
];

let currentIndex = -1;
let isPlaying = false;

function playSong(name) {
    currentIndex = songs.indexOf(name);
    document.getElementById("songName").innerText = name;
    isPlaying = true;
    document.getElementById("playBtn").innerText = "Ⅱ";
}

function togglePlay() {
    if (currentIndex === -1) {
        playSong(songs[0]);
        return;
    }

    isPlaying = !isPlaying;
    document.getElementById("playBtn").innerText =
        isPlaying ? "Ⅱ" : "▶";
}

function nextSong() {
    currentIndex = (currentIndex + 1) % songs.length;
    playSong(songs[currentIndex]);
}

function previousSong() {
    currentIndex = currentIndex <= 0
        ? songs.length - 1 : currentIndex - 1;
    playSong(songs[currentIndex]);
}

function searchMusic() {
    const query = document.getElementById("search")
        .value.toLowerCase();

    document.querySelectorAll(".card[data-name]")
        .forEach(card => {
            card.style.display =
                card.dataset.name.toLowerCase().includes(query)
                ? "block" : "none";
        });
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
