
class GenericSerializer {

    static SerializeToSelectField(element, nameKeyField, nameValueField) {
       return {
           label: element[nameKeyField],
           value: element[nameValueField]
        }
    }

    static SerializeListToSelectField(list, nameKeyField, nameValueField) {
        return list.map(element => this.SerializeToSelectField(element, nameKeyField, nameValueField))
    }
}

export {GenericSerializer}