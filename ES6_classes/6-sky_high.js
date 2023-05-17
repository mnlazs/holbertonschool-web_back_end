import Building from './5-building'

export default class SkyHighBuilding extends Building{
  constructor(sqtf, floors){
    super(sqtf);
    this._floor = floors;
  }

//Methods
evacuationWarningMessage(){
  return 'Evacute slowly the ${this.floor} floors';
  }

//Setters

//Getters
get sqtf() {
    return this._sqft;
  }
get floor() {
    return this._floor;
  }
}