import sender_stand_request
import data
def positive_assert(kit_response, expected_status_code, expected_name):
    assert kit_response.status_code == expected_status_code
    assert kit_response.json()["name"] == expected_name
def negative_assert(kit_response, expected_status_code):
    assert kit_response.status_code == expected_status_code
def test_kit_one_char():
    kit_body = data.kit_bodies["one_char"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    positive_assert(kit_response, 201, kit_body['name'])
def test_kit_max_char():
    kit_body = data.kit_bodies["max_char"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    positive_assert(kit_response, 201, kit_body['name'])
def test_kit_empty_str():
    kit_body = data.kit_bodies["empty_str"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    negative_assert(kit_response, 400)
def test_kit_max_char_plus():
    kit_body = data.kit_bodies["max_char_plus"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    negative_assert(kit_response, 400)
def test_kit_esp_char():
    kit_body = data.kit_bodies["esp_char"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    positive_assert(kit_response, 201, kit_body['name'])
def test_kit_space_char():
    kit_body = data.kit_bodies["space_char"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    positive_assert(kit_response, 201, kit_body['name'])
def test_kit_numbers():
    kit_body = data.kit_bodies["numbers"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    positive_assert(kit_response, 201, kit_body['name'])
def test_kit_no_param():
    kit_body = data.kit_bodies["no_param"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    negative_assert(kit_response, 400)
def test_kit_dif_param():
    kit_body = data.kit_bodies["dif_param"]
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    negative_assert(kit_response, 400)