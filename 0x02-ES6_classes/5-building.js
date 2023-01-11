export default class Building {
  constructor(sqft) {
    if (this.constructor !== Building && !(this.evacuationWarningMessage)) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
    this.sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(sqft) {
      this._sqft = sqft;
  }
}
