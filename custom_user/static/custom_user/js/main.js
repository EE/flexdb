app.directive("customUser", function () {
    return {
        restrict: "E",
        templateUrl: "accounts/useredit/",
        transclude: true
    }
});

function tableControll($scope, $http) {
    $scope.changeUserData = function () {
        $http({
            method: 'PUT',
            url: $scope.user_URL,
            data: angular.toJson($scope.data)
        }).success(function (data) {
                $scope.ajaxDone(data)
            }).error(function () {
                showError("Error occured with connection to the server, please load page again.")
            });
    };
}
