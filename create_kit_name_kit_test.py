import sender_stand_request
import data
def positive_assert(kit_response, expected_status_code, expected_name):
    assert kit_response.status_code == expected_status_code
    assert kit_response.json()["name"] == expected_name

def negative_assert(kit_response, expected_status_code):
    assert kit_response.status_code == expected_status_code

def test_kit_1():
    kit_body = data.kit_bodies["one_char"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    positive_assert(kit_response, 201, kit_body['name'])

def test_kit_2():
    kit_body = data.kit_bodies["max_char"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    positive_assert(kit_response, 201, kit_body['name'])

def test_kit_3():
    kit_body = data.kit_bodies["empty_str"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    negative_assert(kit_response, 400)

def test_kit_4():
    kit_body = data.kit_bodies["max_char_plus"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    negative_assert(kit_response, 400)

def test_kit_5():
    kit_body = data.kit_bodies["esp_char"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    positive_assert(kit_response, 201, kit_body['name'])

def test_kit_6():
    kit_body = data.kit_bodies["space_char"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    positive_assert(kit_response, 201, kit_body['name'])

def test_kit_7():
    kit_body = data.kit_bodies["numbers"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    positive_assert(kit_response, 201, kit_body['name'])

def test_kit_8():
    kit_body = data.kit_bodies["no_param"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    negative_assert(kit_response, 400)

def test_kit_9():
    kit_body = data.kit_bodies["dif_param"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    negative_assert(kit_response, 400)