
class GenericSerializer {

    static SerializeToSelectField(element, nameKeyField, nameValueField) {
       return {
           label: element[nameKeyField],
           value: element[nameValueField]
        }
    }

    static SerializeListToSelectField(list, nameKeyFieldToLabel, nameValueField) {
        return list.map(element => this.SerializeToSelectField(element, nameKeyFieldToLabel, nameValueField))
    }
}

export {GenericSerializer}