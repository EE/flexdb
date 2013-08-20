var myApp = angular.module('flexdb', []).
  config(function($interpolateProvider, $httpProvider){
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  });


function tableControll ($scope, $http){

    $scope.data = {};
    $scope.data.Logged = false;
    $scope.user = {};
    $scope.userid = -1;
    $scope.is_user_data_shown = false;

    function getID () {
        $http({
            method: 'GET',
            url: '/mainPageAjax/getUserData'
        }).success( function  ajaxDone (data) {
            if (data.Logged != null){
                $scope.data.Logged = data.Logged;

                if (data.userid != null){
                    $scope.userid = data.userid;

                }
            }
        });
    }

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
            url: '/accounts/users/'+$scope.userid+'/'
            }).success( function  (data) { ajaxDone(data) });
        if ($scope.data.Logged === true)
            $scope.is_user_data_shown = true;
    }

    $scope.changeUserData = function () {
        $http({
            method: 'PUT',
            url: '/accounts/users/'+$scope.userid+'/',
            data: angular.toJson($scope.data)
            }).success( function  (data) { ajaxDone(data) });
    }

    $scope.hideUserData = function () {
        $scope.is_user_data_shown = false;
    }

    getID();

}
