export default class Token {
  constructor(label, modifier, limit, properties = {}) {
    this.label = label
    this.modifier = modifier
    this.limit = limit
    this.draw_again = properties.draw_again || false
    this.quantity = 0
    this.variable = properties.variable || false
    this.automatic_failure = properties.automatic_failure || false
    this.automatic_success = properties.automatic_success || false
    this.symbol = properties.symbol || false
  }
}
