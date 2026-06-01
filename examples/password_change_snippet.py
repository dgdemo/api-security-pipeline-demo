def update_password(username):
    request_data = request.get_json()
    resp = token_validator(request.headers.get('Authorization'))
    if "error" in resp:
        return Response(error_message_helper(resp), 401, mimetype="application/json")
    else:
        if request_data.get('password'):
            if vuln:  # Unauthorized update of password of another user
                user = User.query.filter_by(username=username).first()
                if user:
                    user.password = request_data.get('password')
                    db.session.commit()
                else:
                    return Response(error_message_helper("User Not Found"), 400, mimetype="application/json")
            else:
                user = User.query.filter_by(username=resp['sub']).first()
                user.password = request_data.get('password')
                db.session.commit()
            responseObject = {
                'status': 'success',
                'Password': 'Updated.'
            }
            return Response(json.dumps(responseObject), 204, mimetype="application/json")
        else:
            return Response(error_message_helper("Malformed Data"), 400, mimetype="application/json")
