const toggleReactions = document.querySelector("#toggle-reactions");
      const reactionsContainer = document.querySelector(".reactions-container");
      toggleReactions.addEventListener("click", function() {
        reactionsContainer.style.display = reactionsContainer.style.display === "flex" ? "none" : "flex";
      });

const reactions = document.querySelectorAll(".reaction");
reactions.forEach(r => {
    r.addEventListener("click", function() {
        reactions.forEach(r => {
        r.classList.remove("selected");
        });
        this.classList.add("selected");
        reactionsContainer.style.display = "none";
    });
});
// Get all reaction buttons
const reactionButtons = document.querySelectorAll('.reaction');

// Add event listener to each reaction button
reactionButtons.forEach(button => {
    button.addEventListener('click', () => {
        const selectedReaction = button.getAttribute('data-reaction');
        console.log(selectedReaction);
    });
});