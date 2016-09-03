/**
 *
 * Created by Kim on 2016. 9. 3..
 */

function join() {
    var form = document.login_form
    var cur_url = location.href
    form.action = '/users/join'
    form.method = "get"
    form.submit()

}
