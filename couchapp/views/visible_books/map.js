function(doc){
    if(doc.visible == true){
        if(doc.TYPE == 'Monograph'){
            emit(doc._id,null);
        }
    }
}
