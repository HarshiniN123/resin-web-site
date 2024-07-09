document.addEventListener("DOMContentLoaded", function() {
    displayPrice(); // Initialize the total price on page load
});

function displayPrice() {
    let frames = document.getElementById('Frames');
    let woodenFrames = document.getElementById('WoodenFrames');
    let keychains = document.getElementById('Keychains');

    let selectedFramePrice = parseInt(frames.value) || 0;
    let selectedWoodenFramePrice = parseInt(woodenFrames.value) || 0;
    let selectedKeychainPrice = parseInt(keychains.value) || 0;

    let totalCost = selectedFramePrice + selectedWoodenFramePrice + selectedKeychainPrice;

    document.getElementById('divprice').innerText = `Total Price: $${totalCost}`;
}
