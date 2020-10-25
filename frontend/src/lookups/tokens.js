import Token from "../classes/token";
export default [
    new Token("+1", 1, 3),
    new Token("0", 0, 4),
    new Token("-1", -1, 5),
    new Token("-2", -2, 4),
    new Token("-3", -3, 3),
    new Token("-4", -4, 2),
    new Token("-5", -5, 2),
    new Token("-6", -6, 1),
    new Token("-7", -7, 1),
    new Token("-8", -8, 1),
    new Token("Blessing", 2, 10, { draw_again: true,  }),
    new Token("Curse", -2, 10, { draw_again: true }),
    new Token("Skull", null, 4, { variable: true, symbol: true }),
    new Token("Cultist", null, 4, { variable: true, symbol: true }),
    new Token("Tablet", null, 4, { variable: true, symbol: true }),
    new Token("Elder Thing", null, 4, { variable: true, symbol: true }),
    new Token("Autofail", 0, 1, { automatic_failure: true }),
    new Token("Elder Sign", null, 1, { variable: true })
]