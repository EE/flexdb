var myApp = angular.module('flexdb', []).
  config(function($interpolateProvider, $httpProvider){
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  });


function tableControll ($scope, $http){

    $scope.data = {};
    $scope.user = {};
    $scope.user_URL = "";
    $scope.is_user_data_shown = false;



    function ajaxDone(data) {
            if (data.username != null) {
                $scope.data.username = data.username;
                $scope.user.username = data.username;
            }
            if (data.first_name != null) {
                $scope.data.first_name = data.first_name;
                $scope.user.first_name = data.first_name;
            }
            if (data.last_name != null) {
                $scope.data.last_name = data.last_name;
                $scope.user.last_name = data.last_name;
            }
            if (data.email != null) {
                $scope.data.email = data.email;
                $scope.user.email = data.email;
            }
        }

    $scope.loadUserData = function () {
        $http({
            method: 'GET',
            url: '/accounts/users/'
            }).success( function  (data) { ajaxDone(data[0]);
                if (data[0].url != null) {
                    $scope.user_URL = data[0].url
                }
            })
            if ($scope.user_URL != null) {
                $scope.is_user_data_shown = true;
            }
    }

    $scope.changeUserData = function () {
        $http({
            method: 'PUT',
            url: $scope.user_URL,
            data: angular.toJson($scope.data)
            }).success( function  (data) { ajaxDone(data) });
    }

    $scope.hideUserData = function () {
        $scope.is_user_data_shown = false;
    }

}
