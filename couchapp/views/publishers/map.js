function(doc) {
    if(doc.TYPE == 'Monograph' && doc.visible === true){
        emit(doc.publisher.toUpperCase().trim(), 1);
    }
}
