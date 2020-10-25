<template>
    <div class="modal is-active" v-if="help">
    {{help}}
        <div class="modal-background" @click="$emit('help', false)"></div>
        <div class="modal-card">
            <header class="modal-card-head">
                <p class="modal-card-title">FAQ and Help</p>
                <button class="delete" aria-label="close" @click="$emit('help', false)"></button>
            </header>
            <section class="modal-card-body">
                <div class="card-content">
                    <p>
                        The panel on the left side of the screen titled
                        <strong>Configure Chaos Bag and Card Effects</strong> is where you set all of the variables. This panel has a table that represents your chaos bag - for each token, you define how many copies are in the bag, and what modifier each token applies to your test result. To use this tool, try the following:
                    </p>
                    <br />
                    <p>
                        <strong>1.</strong> Choose your campaign and difficulty from the
                        <strong>Choose Campaign</strong> dropdown. This will set the quantities of tokens to that campaign/difficulty.
                    </p>
                    <p>
                        <strong>2.</strong> Manually add or remove any tokens that have been added/removed by your campaign by changing the dropdown in the
                        <strong>Quantity</strong> column for that token.
                    </p>
                    <p>
                        <strong>3.</strong> Define the symbol tokens' modifiers by changing the value of the dropdown in the
                        <strong>Effect</strong> column for that token.
                    </p>
                    <p>
                        <small>
                        For example, if the skull token is worth -X where X is the number of ghouls at your location, and there are 3 ghouls at your location, set the
                        <strong>Effect</strong> for skull to -3.
                        </small>
                    </p>
                    <p>
                        <strong>4.</strong> Set any other token effects, such as
                        <strong>Draw Again</strong> or
                        <strong>Automatically Fails</strong>
                    </p>
                    <p>
                        <strong>5.</strong> Choose a character from the
                        <strong>Choose Character</strong> dropdown. This will set the effect of the Elder Sign token, as well as apply and specific effects for investigators like Jim Culver or Father Mateo. If the chosen character's elder sign ability is variable, you may need to manually specify their effect.
                    </p>
                    <p>
                        <strong>6.</strong> Select the
                        <strong>Card Effects</strong> tab to select any cards you may be using for this skill test.
                    </p>
                </div>
            </section>
            <footer class="modal-card-foot">
                <button class="button" @click="$emit('help', false)">Got it!</button>
            </footer>
        </div>
    </div>
</template>
<script>
export default {
    name: "helpModal",
    props: {
        help: {
            required: true,
            type: Boolean
        }
    }
}