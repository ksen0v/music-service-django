const audioPlayer = document.getElementById('audio-player');
const audioElement = document.querySelector("audio");
const playPauseBtn = document.getElementById('play-pause-btn');
const playIcon = document.getElementById('play-icon');
const currentTimeElement = document.getElementById("current-time");
const progressBar = document.querySelector('.progress-bar');
const progress = document.getElementById('progress');
const durationElement = document.getElementById("duration");

// Play/Pause
function togglePlayPause() {
    if (audioPlayer.paused) {
        audioPlayer.play();
        playIcon.classList.remove('fa-play');
        playIcon.classList.add('fa-pause');
    } else {
        audioPlayer.pause();
        playIcon.classList.remove('fa-pause');
        playIcon.classList.add('fa-play');
    }
}

// Форматирование времени в формате MM:SS
function formatTime(time) {
    const minutes = Math.floor(time / 60);
    const seconds = Math.floor(time % 60);
    return `${minutes}:${seconds < 10 ? "0" : ""}${seconds}`;
}

// Отображает длительность трека
audioElement.addEventListener("loadedmetadata", () => {
    const duration = audioElement.duration; // Получает общую длительность трека
    durationElement.textContent = formatTime(duration);
});

// Обновляет время прослушивания терка
audioElement.addEventListener("timeupdate", () => {
    // Обновляет текущее время
    const currentTime = audioElement.currentTime;
    currentTimeElement.textContent = formatTime(currentTime);

    // Обновляет прогресс-бар
    const percent = (currentTime / audioElement.duration) * 100;
    progress.style.width = `${percent}%`;
});

// Перематывание трека
function setProgress(event) {
    const barWidth = progressBar.clientWidth;
    const clickX = event.offsetX;
    const duration = audioElement.duration;

    audioElement.currentTime = (clickX / barWidth) * duration;
}

// Заглушки для переключения треков
function prevTrack() {
    alert('Предыдущий трек');
}

function nextTrack() {
    alert('Следующий трек');
}

document.addEventListener('DOMContentLoaded', () => {
    const audioPlayer = document.getElementById('audio-player');
    const volumeSlider = document.getElementById('volume-slider');
    const volumeDownBtn = document.getElementById('volume-down-btn');
    const volumeUpBtn = document.getElementById('volume-up-btn');

    const trackLogo = document.getElementById('track-logo');
    const trackTitle = document.getElementById('track-title');
    const trackAuthor = document.getElementById('track-author');
    // Изменение громкости через ползунок
    volumeSlider.addEventListener('input', (e) => {
        audioPlayer.volume = e.target.value;
    });

    // Уменьшение громкости кнопкой
    volumeDownBtn.addEventListener('click', () => {
        audioPlayer.volume = Math.max(audioPlayer.volume - 0.1, 0);
        volumeSlider.value = audioPlayer.volume;
    });

    // Увеличение громкости кнопкой
    volumeUpBtn.addEventListener('click', () => {
        audioPlayer.volume = Math.min(audioPlayer.volume + 0.1, 1);
        volumeSlider.value = audioPlayer.volume;
    });

    document.querySelectorAll('.track').forEach(track => {
        track.addEventListener('click', function () {
            const trackSrc = this.getAttribute('data-src');
            const logoSrc = this.getAttribute('data-logo');
            const trackName = this.getAttribute('data-name');
            const trackAuthorName = this.getAttribute('data-author');

            if (trackSrc) {
                // Обновляем источник и воспроизводим
                audioPlayer.src = trackSrc;
                audioPlayer.play();

                // Обновляем текст и изображение
                trackLogo.src = logoSrc;
                trackTitle.textContent = trackName;
                trackAuthor.textContent = trackAuthorName;

                // Меняем иконку на паузу
                playIcon.classList.remove('fa-play');
                playIcon.classList.add('fa-pause');
            }
        });
    });

    // Обработчик для кнопки play/pause
    playButton.addEventListener('click', function () {
        if (audioPlayer.paused) {
            audioPlayer.play();
            playIcon.classList.remove('fa-play');
            playIcon.classList.add('fa-pause');
        } else {
            audioPlayer.pause();
            playIcon.classList.remove('fa-pause');
            playIcon.classList.add('fa-play');
        }
    });
});
