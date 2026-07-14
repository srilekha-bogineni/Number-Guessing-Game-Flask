console.log("JavaScript Connected");
const difficultySelect = document.querySelector("select[name='difficulty']");
const hiddenDifficulty = document.getElementById("selectedDifficulty");

if (difficultySelect && hiddenDifficulty) {

    hiddenDifficulty.value = difficultySelect.value;

    difficultySelect.addEventListener("change", function () {
        hiddenDifficulty.value = this.value;
    });

}