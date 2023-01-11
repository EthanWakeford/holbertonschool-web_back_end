export default class Building {
  constructor(sqft) {
    this.sqft = sqft;
    if (this.constructor !== Building && !(this.evacuationWarningMessage)) {
      throw new Error('Class extending Building must override evacuationWarningMessage')
    }
  }

  get sqft() {
    return this.sqft;
  }

  set sqft(sqft) {
    if (typeof sqft === 'number') {
      this._sqft = sqft;
    } else {
      throw new TypeError('sqft must be a number');
    }
  }
}
