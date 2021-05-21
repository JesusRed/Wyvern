def import_favs(request):
    total = 0
    if request.user.is_authenticated:
        for key, value in request.session["favs"].items():
            total = total+(float(value["cantidad"]))
    return {"import_favs": total}
