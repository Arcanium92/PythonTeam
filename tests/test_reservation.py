from library_app.reservation import Reservation, ReservationStatus

def test_new_reservation_starts_with_pending_status():
    # Arrange
    reservation = Reservation("0000000000000", "Sample Customer")

    # Act
    status = reservation.status

    # Assert
    assert status == ReservationStatus.PENDING

def test_cancel_sets_status_to_cancelled():
    # Arrange
    reservation = Reservation("0000000000000", "Sample Customer")

    # Act
    reservation.cancel()

    # Assert
    assert reservation.status == ReservationStatus.CANCELLED

def test_cancel_raises_error_when_reservation_is_not_pending():
    # Arrange
    reservation = Reservation("0000000000000", "Sample Customer")
    reservation.is_complete()

    error_raised = False

    # Act
    try:
        reservation.cancel()
    except RuntimeError:
        error_raised = True

    # Assert
    assert error_raised